import pandas as pd
import plotly.express as px
from django.http import JsonResponse
from django.shortcuts import render
from .models import ImpedanceData

def upload_and_plot(request):
    if request.method != 'POST' or not request.FILES['file']:
        return render(request, 'upload.html')
    # Upload the CSV file
    csv_file = request.FILES['file']
    data = pd.read_csv(csv_file)

    # Ensure 'Re' and 'Rct' fields are numeric (handle invalid values)
    data['Re'] = pd.to_numeric(data['Re'], errors='coerce')
    data['Rct'] = pd.to_numeric(data['Rct'], errors='coerce')

    # Drop rows where 'Re' or 'Rct' could not be converted to numbers
    data = data.dropna(subset=['Re', 'Rct'])

    # If aging is based on test_id, we can use it directly.
    # If aging is based on start_time, calculate the time difference in days from the first test.
    if 'test_id' in data.columns:
        data['Aging'] = data['test_id']  # Using test_id as aging (cycle number or test sequence)
    elif 'start_time' in data.columns:
        # Calculate aging based on time difference from the first entry
        data['start_time'] = pd.to_datetime(data['start_time'])
        data['Aging'] = (data['start_time'] - data['start_time'].min()).dt.days  # Aging in days

    # Calculate Battery Impedance
    data['Battery_Impedance'] = data['Re'] + data['Rct']

    # Create the plots using Plotly
    fig_re = px.scatter(
        data,
        x='Aging',  # Aging progression (either by test_id or by time)
        y='Re',
        title='Electrolyte Resistance (Re) vs Aging',
        labels={'Aging': 'Aging (Cycles/Days)', 'Re': 'Electrolyte Resistance (Ohms)'},
        trendline="lowess"
    )

    fig_rct = px.scatter(
        data,
        x='Aging',
        y='Rct',
        title='Charge Transfer Resistance (Rct) vs Aging',
        labels={'Aging': 'Aging (Cycles/Days)', 'Rct': 'Charge Transfer Resistance (Ohms)'},
        trendline="lowess"
    )

    fig_impedance = px.scatter(
        data,
        x='Aging',
        y='Battery_Impedance',
        title='Battery Impedance vs Aging',
        labels={'Aging': 'Aging (Cycles/Days)', 'Battery_Impedance': 'Battery Impedance (Ohms)'},
        trendline="lowess"
    )

    # Convert the plots to HTML to embed them into the Django template
    plot_re = fig_re.to_html(full_html=False)
    plot_rct = fig_rct.to_html(full_html=False)
    plot_impedance = fig_impedance.to_html(full_html=False)

    return render(request, 'plot.html', {
        'plot_re': plot_re,
        'plot_rct': plot_rct,
        'plot_impedance': plot_impedance
    })
