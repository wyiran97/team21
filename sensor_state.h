/* ************************************************************************** */
/** 
  @Course
    Summer2019 ECE 4534
 
  @File Name
    sensor_state.h

  @Edited
    team 21
 */
/* ************************************************************************** */

#ifndef _SENSOR_STATE_H    /* Guard against multiple inclusion */
#define _SENSOR_STATE_H


#include <FreeRTOS.h>
#include "queue.h"
#include "sensor_queue.h"
#include "debug.h"
#include "system_config.h"
#include "system_definitions.h"

#define SAMPLE_TIMES 0x05
#define BUFFER_SIZE 0x02
#define IN_DECIMAL 0x0a
typedef enum {ONE, TWO, THREE, FOUR, FIVE}sensorState;

void runStateMachine(int *sum, Message messageValue, sensorState *currentState);
void printOutAverage(int average, Message msg);

/* Provide C++ Compatibility */
#ifdef __cplusplus
extern "C" {
#endif

    /* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _EXAMPLE_FILE_NAME_H */

/* *****************************************************************************
 End of File
 */
