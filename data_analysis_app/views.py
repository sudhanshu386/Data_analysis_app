from django.shortcuts import render

# Create your views here.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from django.shortcuts import render
from .forms import CSVUploadForm

def upload_file(request):
    error_message = None
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                df = pd.read_csv(file)
                # Inspect the first few rows of the dataframe
                head = df.head().to_html()
                summary = df.describe().to_html()
                
                # Trying to handle missing values
                df = df.apply(pd.to_numeric, errors='coerce')
                df = df.fillna(df.mean())

                # Visualization
                plt.figure(figsize=(10, 4))
                img = io.BytesIO()
                sns.histplot(df.select_dtypes(include='number').iloc[:, 0]).figure.savefig(img, format='png')
                img.seek(0)
                plot_url = base64.b64encode(img.getvalue()).decode()

                return render(request, 'results.html', {
                    'head': head,
                    'summary': summary,
                    'plot_url': 'data:image/png;base64,{}'.format(plot_url)
                })
            except Exception as e:
                error_message = str(e)

    else:
        form = CSVUploadForm()

    return render(request, 'upload.html', {'form': form, 'error_message': error_message})
