/* ************************************************************************** */
/** 
  @Course
    Summer2019 ECE 4534
 
  @File Name
    debug.h

  @Edited
    team 21
 */
/* ************************************************************************** */

#ifndef _SENSOR_QUEUE_H    /* Guard against multiple inclusion */
#define _SENSOR_QUEUE_H

#include <stdio.h>
#include <FreeRTOS.h>
#include "queue.h"
#include "system_config.h"
#include "system_definitions.h"

QueueHandle_t Globle_Queue;
typedef struct {
    unsigned int sensorVal;
    char units[11];     //centimeters
}Message;


void Queue_Initialize();
Message ReceiveFromQueue();
void SendSensorToQueue(BaseType_t *pxHigherPriorityTaskWoken);
unsigned int ConversionFromADC(unsigned int value);

/* Provide C++ Compatibility */
#ifdef __cplusplus
extern "C" {
#endif


 
    /* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _SENSOR_QUEUE_H */

/* *****************************************************************************
 End of File
 */
