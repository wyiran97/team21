/* ************************************************************************** */
/** 
  @Course
    Summer2019 ECE 4534
 
  @File Name
    sensor_queue.h

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
#include <math.h>

#define QUEUE_SIZE 0x0f
#define UNITS_SIZE 0x0b
#define LUT_SIZE 0x40
#define ADC_SHIFT 0x04
#define DIS_SHIFT 0x05
typedef struct {
    unsigned int sensorVal;
    char units[UNITS_SIZE];     //centimeters
}Message;

QueueHandle_t msgQueue;
void Queue_Initialize();
Message ReceiveFromQueue();
void SendSensorToQueue(BaseType_t pxHigherPriorityTaskWoken);
Message ConversionFromADC(unsigned int value);

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
