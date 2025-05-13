from typing import List, Dict

import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

def get_distribuciontenencia() -> List[Dict[str, str]]:
    
    response = requests.get("https://www.banxico.org.mx/apps/dao-web/4/20/distribuciontenencia.html")
    soup = BeautifulSoup(response.text, 'html.parser')

    distribuciontenencia = []
    
    Title = ''
    Value = ''
    Figure = ''
    for item in soup.find_all("tr"):
        if 'class' in item.attrs and 'banxicotitle2' in item.attrs['class']:
            
            titles = [x.strip() for x in item.text.split('\n') if x.strip()!='']
            Title = titles[0]
            Value = titles[1]
            Figure = titles[2]
        
        if 'class' in item.attrs and 'banxicotablerow' in item.attrs['class'][0]:
            
            tds = item.find_all("td")
            date_str = tds[1].text.strip()
            if '/' in date_str:

                CI = tds[0].text.strip()
                
                date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")  # Parse as DD/MM/YYYY
                FechaDeVencimiento = date_obj.strftime("%Y-%m-%d")  # Format as YYYY-MM-DD

                ReportosConBanxico = float(tds[2].text.replace(",", "").strip())
                GarantiasRecibidasPorBanxico = float(tds[3].text.replace(",", "").strip())
                ValoresAdquiridosPorBanxico = float(tds[4].text.replace(",", "").strip())
                SectorBancario = float(tds[5].text.replace(",", "").strip())
                SieforesYSociedadesDeInversion = float(tds[6].text.replace(",", "").strip())
                AseguradorasYAfianzadoras = float(tds[7].text.replace(",", "").strip())
                OtrosResidentesEnElPais = float(tds[8].text.replace(",", "").strip())
                ResidentesEnElPais = float(tds[9].text.replace(",", "").strip())
                ResidentesEnElExtranjero = float(tds[10].text.replace(",", "").strip())
                TotalEnCirculacion = float(tds[11].text.replace(",", "").strip())

                distribuciontenencia.append({"scrape_datetime": datetime.datetime.utcnow().isoformat() + "Z", "Title": Title, "Value": Value, "Figure": Figure, "CI": CI, "FechaDeVencimiento": FechaDeVencimiento,
                                "ReportosConBanxico": ReportosConBanxico, "GarantiasRecibidasPorBanxico": GarantiasRecibidasPorBanxico, 
                                "ValoresAdquiridosPorBanxico": ValoresAdquiridosPorBanxico, "SectorBancario": SectorBancario, "SieforesYSociedadesDeInversion": SieforesYSociedadesDeInversion,
                                "AseguradorasYAfianzadoras": AseguradorasYAfianzadoras, "OtrosResidentesEnElPais": OtrosResidentesEnElPais, "ResidentesEnElPais": ResidentesEnElPais,
                                "ResidentesEnElExtranjero": ResidentesEnElExtranjero, "TotalEnCirculacion": TotalEnCirculacion})

    return distribuciontenencia           
        

def run(filename: str):

    """
    This function will be the main entrypoint to your code and will be called with a filename.
    """
    
    distribuciontenencia = get_distribuciontenencia()

    output = pd.DataFrame(distribuciontenencia)
        
    output.to_csv(
        filename,
        encoding="utf-8",
        quotechar='"',
        index=False
    )
