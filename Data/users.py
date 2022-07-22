import json


Admin_Naimix = json.dumps({"login": "nmadmin", "password": "nmadmin123"})
Manager_Naimix = json.dumps({'login': 'mm@list.ru', 'password': 'Www1234!'})

q = json.dumps({"clientId": "405f967d-dedd-4a3d-9348-71c21cf3410a",
           "pageNum": 1,
           "pageSize": 25,
           "archiveFilter": False,
           "fioSort": "asc",
           "needToEnrichPhantomUsersByClientInfo": True,
           "fioFilter": "павел"
           }
          )




payload = {
  "representativePhone": "72343111231",
  "representativeEmail": "vasya1pupk2453@gmail.com",
  "inn": "8282305891",
  "clientType": "RUSSIAN_LEGAL_ENTITY",
  "registeredAddress": "Алтайский край",
  "representativeName": "ываыва ываываыв ываываыв",
  "name": "sdfsdfsdf",
  "fullName": "fdsfsdfsdf sdfsdfds sdf sdfsd",
  "brand": "sdfsdfsdf",
  "currentCommissionRate": 0.02,
  "civilPaymentCommission": 0.02,
  "contractorCivilOrderPaymentsCommission": 0.04,
  "contractorCivilRegistryPaymentsCommission": 0.04,
  "contractorSmzOrderPaymentsCommission": 0.04,
  "contractorSmzRegistryPaymentsCommission": 0.04,
  "insuranceAvailable": False,
  "categoryId": "e66ba158-f2e3-4d97-a564-e4dfb6a7d0da",
  "ordersLimit": 0,
  "civilOrdersLimit": 0,
  "registryPaymentsAvailable": False,
  "civilRegistryPaymentsAvailable": False,
  "ordersUnsecured": True,
  "edmAvailable": True,
  "withoutContract": False,
  "minCommissionAmount": 40,
  "paymentsThresholdAmount": 3000,
  "depositDistributedByObjects": False
}

titi = {
"clientId":"405f967d-dedd-4a3d-9348-71c21cf3410a",
 "pageNum":1,
 "pageSize":25,
 "archiveFilter": False,
 "fioSort":"asc",
 "needToEnrichPhantomUsersByClientInfo": True,
 "emailFilter":"wow"
}

