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
#ifndef _DEBUG_H_
#define _DEBUG_H_


#include "system/common/sys_module.h"
#include "system_config.h"
#include "system_definitions.h"

//indicate queue is running correct
#define DLOC_TASK_BEGIN 0x01
#define DLOC_RECEIVE_FROM_QUEUE_BEGIN 0x02
#define DLOC_RECEIVE_FROM_QUEUE_END 0x03
#define DLOC_SEND_TO_QUEUE_BEGIN 0x04
#define DLOC_SEND_TO_QUEUE_END 0x05
#define DLOC_ENTER_ISR 0x06
#define DLOC_LEAVE_ISR 0x07

//indicate the state machine is running correct
#define DLOC_STATE_ONE 0x11
#define DLOC_STATE_TWO 0x12
#define DLOC_STATE_THREE 0x13
#define DLOC_STATE_FOUR 0x14
#define DLOC_STATE_FIVE 0x15
#define DLOC_STATE_ERROR 0x16

//indicate some errors happen during send and receive message
#define STOP_NO_RECEIVE 0x21
#define STOP_NO_SEND 0x22
#define STOP_CREATE_ERROR 0x23

void dbgOutputVal(unsigned int outVal);
void dbgOutputLoc(unsigned int outVal);
char dbgUARTVal(unsigned char outVal);
void stop(unsigned int outVal);
/* Provide C++ Compatibility */
#ifdef __cplusplus
extern "C" {
#endif


    /* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _DEBUG_H */

/* *****************************************************************************
 End of File
 */
