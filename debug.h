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

void dbgOutputVal(unsigned int outVal);
void dbgOutputLoc(unsigned int outVal);
char dbgUARTVal(unsigned char outVal);
void stop();
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
