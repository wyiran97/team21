/* ************************************************************************** */
/** Descriptive File Name

    @Course
        Summer2019 ECE 4534
 
    @File Name
         sensor_state.c

    @Edited
         team 21
 */
/* ************************************************************************** */

#include "sensor_state.h"
#include "debug.h"
#include "sensor_queue.h"

void runStateMachine(int *sum, Message messageValue, sensorState *currentState)
{
    switch(*currentState)
    {
        case ONE:
            dbgOutputLoc(DLOC_STATE_ONE);
            dbgOutputVal(messageValue.sensorVal);
            *sum = *sum + messageValue.sensorVal;
            *currentState = TWO;
            break;
        case TWO:
            dbgOutputLoc(DLOC_STATE_TWO);
            dbgOutputVal(messageValue.sensorVal);
            *sum = *sum + messageValue.sensorVal;
            *currentState = THREE;
            break;
        case THREE:
            dbgOutputLoc(DLOC_STATE_THREE);
            dbgOutputVal(messageValue.sensorVal);
            *sum = *sum + messageValue.sensorVal;
            *currentState = FOUR;
            break;
        case FOUR:
            dbgOutputLoc(DLOC_STATE_FOUR);
            dbgOutputVal(messageValue.sensorVal);
            *sum = *sum + messageValue.sensorVal;
            *currentState = FIVE;
            break;
        case FIVE:
            dbgOutputLoc(DLOC_STATE_FIVE);
            dbgOutputVal(messageValue.sensorVal);
            *sum = *sum + messageValue.sensorVal;
            *currentState = ONE;
            int avgValue = *sum / SAMPLE_TIMES;
            *sum = 0;
            printOutAverage(avgValue, messageValue);
            break;
        default:
            dbgOutputLoc(DLOC_STATE_ERROR);
    }
}

void printOutAverage(int average, Message msg)
{
    char buffer[BUFFER_SIZE];
    itoa(buffer,average, IN_DECIMAL);
    dbgUARTVal(buffer[0]);
    dbgUARTVal(buffer[1]);
    int i;
    for (i = 0; i < UNITS_SIZE; i++)
    {
        dbgUARTVal(msg.units[i]);
    }
}

/* *****************************************************************************
 End of File
 */
