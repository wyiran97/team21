/* 
 * File:   sensor_state.h
 * Author: team 21
 *
 * Created on June 5, 2019, 3:52 PM
 */

#ifndef SENSOR_STATE_H
#define	SENSOR_STATE_H
#include <FreeRtos.h>
#include <queue.h>
#include "debug.h"
#include "sensor_queue.h"

typedef enum {state1,state2,state3,state4,state5} status;
void runstate(status *current,int *sumValue, Message messageValue);
void printoutAverage(int averagess);








#ifdef	__cplusplus
extern "C" {
#endif




#ifdef	__cplusplus
}
#endif

#endif	/* SENSOR_STATE_H */

