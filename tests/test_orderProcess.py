# from src.geocloudservice.schedule.orderProcess import OrderProcess
from data_extraction_service.external.schedule.orderProcess import OrderProcess

myOrderProcess = OrderProcess()
myOrderProcess.writeOrderData()
# myOrderProcess.justForTest()
# myOrderProcess.readOrderData()