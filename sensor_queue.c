/* ************************************************************************** */
/** Descriptive File Name

    @Course
        Summer2019 ECE 4534
 
    @File Name
    sensor_queue.c

    @Edited
         team 21
 */
/* ************************************************************************** */

#include "sensor_queue.h"
#include "debug.h"


/*
 * create queue
 */
void Queue_Initialize()
{
    DRV_ADC_Open();
    DRV_ADC_Start();
    DRV_TMR0_Start();
    msgQueue = xQueueCreate(QUEUE_SIZE,sizeof(Message));
    if (msgQueue == NULL)
    {
        stop(STOP_CREATE_ERROR);
    }
}


/*
 * sensor value receive from a queue
 */
Message ReceiveFromQueue()
{
    Message result;
    dbgOutputLoc(DLOC_RECEIVE_FROM_QUEUE_BEGIN);
    if (xQueueReceive(msgQueue, &result, portMAX_DELAY))
    {
        dbgOutputLoc(DLOC_RECEIVE_FROM_QUEUE_END);
        return result;
    }
    else
    {
        stop(STOP_NO_RECEIVE);
    }
}



/*
 * put message into queue from ISR
 */
void SendSensorValToQueue(BaseType_t pxHigherPriorityTaskWoken)
{
    Message msg;
    msg = ConversionFromADC(DRV_ADC_SamplesRead(0));
    dbgOutputLoc(DLOC_SEND_TO_QUEUE_BEGIN);
    if (xQueueSendToBackFromISR(msgQueue, &msg, &pxHigherPriorityTaskWoken) == pdPASS)
    {
        dbgOutputLoc(DLOC_SEND_TO_QUEUE_END);  //send successfully
    }
    else
    {
      stop(STOP_NO_SEND);
    }
}

Message ConversionFromADC(unsigned int value)
{
    Message msg;
    char tempUnits[UNITS_SIZE] = "centimeters";
    int i;
    for (i = 0; i < UNITS_SIZE; i++)
    {
        msg.units[i] = tempUnits[i];
    }
    
    //formula: 108534.81*pow((value*3300/1024),-1.2);
    int adcArray[] = { 26651,11600,7131,5049,3863,3104,2580,2198,1908,1682,1500,1351,1227,1123,1034,957, 
                        890,831,778,732,690,653,619,588,560,534,511,489,469,450,433,416,401,387,374,362, 
                        350,339,328,319,309,300,292,284,277,269,263,256,250,244,238,233,227,222,217,213,208, 
                        204,200,196,192,188,185,181};
    
    if (value >= 1 && value <= LUT_SIZE)
    {
        msg.sensorVal = adcArray[value - 1];
    }
    else
    {
        value = value >> ADC_SHIFT;
        msg.sensorVal = (adcArray[value - 1] >> DIS_SHIFT) + 2;
    }
    return msg;
}
/* *****************************************************************************
 End of File
 */
