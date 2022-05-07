from fhirclient import client
import fhirclient.models.patient as p

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://server.fire.ly/r4	'
}

smart = client.FHIRClient(settings=settings)

patient = p.Patient.read('f001', smart.server)
print('Birth Date', patient.birthDate.isostring)
print('Patient Name', smart.human_name(patient.name[0]))