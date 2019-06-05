/* ************************************************************************** */
/** Descriptive File Name

  @Company
    Company Name

  @File Name
    filename.c

  @Summary
    Brief description of the file.

  @Description
    Describe the purpose of this file.
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
    DRV_TMR0_Start();
    Globle_Queue = xQueueCreate(6,sizeof(Message));
    if (Globle_Queue == NULL)
    {
        stop(0x08);
    }
}

/*
 * sensor value receive from a queue
 */
Message ReceiveFromQueue()
{
    Message result;
    dbgOutputLoc(DLOC_RECEIVE_FROM_QUEUE_BEGIN);
    if (xQueueReceive(Globle_Queue, &result, portMAX_DELAY))
    {
         dbgOutputLoc(DLOC_RECEIVE_FROM_QUEUE_END);
         return result;
    }
    else
    {
        stop(0x11);
    }
}



/*
 * put message into queue from ISR
 */
void SendSensorValToQueue(BaseType_t *pxHigherPriorityTaskWoken)
{
    dbgOutputLoc(DLOC_SEND_TO_QUEUE_BEGIN);
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
    unsigned int sensorValue;
    unsigned int sensorValConvert;
    
    
    sensorValue = DRV_ADC_SamplesRead(0);
    sensorValConvert = ConversionFromADC(sensorValue);
    DRV_ADC_Start();
    
    msg.sensorVal = sensorValConvert;
    if (xQueueSendToBackFromISR(Globle_Queue, &msg, pxHigherPriorityTaskWoken))
    {
        dbgOutputLoc(DLOC_SEND_TO_QUEUE_END);  //send successfully
    }
    else
    {
        stop(0x09);
    }
}

unsigned int ConversionFromADC(unsigned int value)
{
    unsigned int result;
    unsigned int voltageRatio = 1023/3.3 * value;
    result = 4.8 / (voltageRatio - 0.02);
    return result;
}

/* *****************************************************************************
 End of File
 */
