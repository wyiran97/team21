/* ************************************************************************** */
/** Descriptive File Name

    @Course
        Summer2019 ECE 4534
 
    @File Name
         debug.h

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
    Globle_Queue = xQueueCreate(15,sizeof(Message));
    if (Globle_Queue == NULL)
    {
        stop(STOP_CREATE_ERROR);
    }
}


/*
 * sensor value receive from a queue
 */
Message ReceiveFromQueue()
{
    dbgOutputLoc(DLOC_RECEIVE_FROM_QUEUE_BEGIN);
    Message result;
    
    if (xQueueReceive(Globle_Queue, &result, portMAX_DELAY) == pdTRUE)
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
    dbgOutputLoc(DLOC_SEND_TO_QUEUE_BEGIN);
    Message msg;
    
    msg = ConversionFromADC(DRV_ADC_SamplesRead(0));
    if (xQueueSendToBackFromISR(Globle_Queue, &msg, &pxHigherPriorityTaskWoken) == pdPASS)
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
    msg.units[0] = 'c';
    msg.units[1] = 'e';
    msg.units[2] = 'n';
    msg.units[3] = 't';
    msg.units[4] = 'i';
    msg.units[5] = 'm';
    msg.units[6] = 'e';
    msg.units[7] = 't';
    msg.units[8] = 'e';
    msg.units[9] = 'r';
    msg.units[10] = 's';
    msg.sensorVal = 108534.81*pow((value*3300/1024),-1.2);
    return msg;
}
/* *****************************************************************************
 End of File
 */
