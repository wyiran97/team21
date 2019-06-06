
#include "sensor_state.h"

void runstate(status *current,int *sumValue, Message messageValue)
{
    switch(*current){
        case(state1):
           dbgOutputVal(messageValue.sensorVal);
           *sumValue = *sumValue + messageValue.sensorVal;
           *current = state2;
           break;
        case(state2):
           dbgOutputVal(messageValue.sensorVal);
           *sumValue = *sumValue + messageValue.sensorVal;
           *current = state3;
           break;
        case(state3):
           dbgOutputVal(messageValue.sensorVal);
           *sumValue = *sumValue + messageValue.sensorVal;
           *current = state4;
           break;
        case(state4):
           dbgOutputVal(messageValue.sensorVal);
           *sumValue = *sumValue + messageValue.sensorVal;
           *current = state5;
           break;
        case(state5):
            dbgOutputVal(messageValue.sensorVal);
            *sumValue = *sumValue + messageValue.sensorVal;
            *current = state1;
            int average = *sumValue/5;
            printoutAverage(average);
            *sumValue = 0;
    }
}

void printoutAverage(int average)
{
    char n[3];
    itoa(n,average,10);
    dbgUARTVal(n[0]);
    dbgUARTVal(n[1]);
    dbgUARTVal(n[2]);
    dbgUARTVal(n[3]);
}