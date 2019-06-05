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
#include "debug.h"
void dbgOutputVal(unsigned int outVal)
{
    if (outVal <= 127)
    {
        PLIB_PORTS_Write(PORTS_ID_0, PORT_CHANNEL_E, outVal);
        PLIB_PORTS_PinToggle(PORTS_ID_0, PORT_CHANNEL_E, PORTS_BIT_POS_7);
    }
}

void dbgOutputLoc(unsigned int outVal)
{
    if (outVal <= 127)
    {
        PLIB_PORTS_Write(PORTS_ID_0, PORT_CHANNEL_D, outVal);
        PLIB_PORTS_PinToggle(PORTS_ID_0, PORT_CHANNEL_D, PORTS_BIT_POS_7);
    }
}

char dbgUARTVal(unsigned char outVal)
{
    DRV_USART0_WriteByte(outVal); 
    return outVal;
}

void stop(unsigned int outVal)
{
    SYS_INT_Disable();
    vTaskSuspendAll();
    while (1)
    {
        dbgOutputLoc(outVal); //if stop everything, output 127 in decimal
    }
}
/* *****************************************************************************
 End of File
 */
