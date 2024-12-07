import pandas as pd
import plotly.express as px
from django.http import JsonResponse
from django.shortcuts import render
from .models import ImpedanceData

def upload_and_plot(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']
        data = pd.read_csv(csv_file)
        
        # Extract the real parts of 'Re' and 'Rct'
        def extract_real(value):
            try:
                complex_value = complex(value)
                return complex_value.real
            except (ValueError, TypeError):
                return None

        data['Re'] = data['Re'].apply(extract_real)
        data['Rct'] = data['Rct'].apply(extract_real)
        data = data.dropna(subset=['Re', 'Rct'])
        
        # Calculate Battery Impedance
        data['Battery_Impedance'] = data['Re'] + data['Rct']
        
        # Create the plots
        fig_re = px.scatter(
            data,
            x='test_id',
            y='Re',
            title='Electrolyte Resistance (Re) vs Aging',
            labels={'test_id': 'Test ID (Aging)', 'Re': 'Electrolyte Resistance (Ohms)'},
            trendline="lowess"
        )
        fig_rct = px.scatter(
            data,
            x='test_id',
            y='Rct',
            title='Charge Transfer Resistance (Rct) vs Aging',
            labels={'test_id': 'Test ID (Aging)', 'Rct': 'Charge Transfer Resistance (Ohms)'},
            trendline="lowess"
        )
        fig_impedance = px.scatter(
            data,
            x='test_id',
            y='Battery_Impedance',
            title='Battery Impedance vs Aging',
            labels={'test_id': 'Test ID (Aging)', 'Battery_Impedance': 'Battery Impedance (Ohms)'},
            trendline="lowess"
        )
        
        # Convert plots to JSON for rendering
        plot_re = fig_re.to_html(full_html=False)
        plot_rct = fig_rct.to_html(full_html=False)
        plot_impedance = fig_impedance.to_html(full_html=False)
        
        return render(request, 'plot.html', {
            'plot_re': plot_re,
            'plot_rct': plot_rct,
            'plot_impedance': plot_impedance
        })
    return render(request, 'upload.html')
