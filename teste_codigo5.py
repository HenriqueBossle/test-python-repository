from datetime import datetime, timedelta


hoje = datetime.now()

print(hoje.date())

semana= hoje + timedelta(weeks=1)

print(semana.date())