import json
import time
import requests
import logging


def url_scan(url):
    urls = []
    urls.append(url)
    api_key = "a4046034c0e7075157cd3e5292e9f36b896ce917a4bf042d0e567c8a1ce46e4f"
    VT = "https://www.virustotal.com/vtapi/v2/url/report"

    try:
        for site in urls:
            params = {"apikey": api_key, 'resource': site}
            response = requests.get(VT, params=params)
            response_json = json.loads(response.content)

            if response_json['positives'] <= 0:
                with open('vt_report.txt', 'a') as vt:
                    vt.write(site) and vt.write("- \tNo es peligroso\n")

            elif response_json['positives'] >= 2:
                with open('vt_report.txt', 'a') as vt:
                    vt.write(site) and vt.write("- \tPodria ser peligroso\n")

            elif response_json['positives'] >= 4:
                with open('vt_report.txt', 'a') as vt:
                    vt.write(site) and vt.write("- \tTen cuidado\n")
            else:
                print("<%s> not found" % site)
            time.sleep(3)
            print("Se a creado exitosamente el reporte")
    except KeyError:
        logging.basicConfig(filename='app.log', level='DEBUG')
        logging.error("No se pudo encontrar el reporte de la Url: %s" %(site))
        print("A occurido un error de conexion")

if __name__ == '__main__':
    url = input("Ingresa tu url:\n")
    url_scan(url)


