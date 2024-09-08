
from django.shortcuts import render
import io
import urllib,base64
import seaborn as sns

def home (request) :
    sns.set_theme(style="ticks")
    df = sns.load_dataset("anscombe")

    fig = sns.lmplot(
    data=df, x="x", y="y", col="dataset", hue="dataset",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1})
    
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    
    return render(request,'home.html',{'data':uri})
