import platform


VERSION_MAJOR = 0
VERSION_MINOR = 7
VERSION_RELEASE = 0
VERSION_NUMBER = "0.7.0"
VERSION = "0.7.0"

REVISION = 12230

HANDLE_INVALID = 0

TPDEVICEHANDLE_INVALID = HANDLE_INVALID

INTERFACE_DEVICE = 0x0000000000000001
INTERFACE_OSCILLOSCOPE = 0x0000000000000002
INTERFACE_GENERATOR = 0x0000000000000004
INTERFACE_I2CHOST = 0x0000000000000008

DEVICETYPE_OSCILLOSCOPE = 0x00000001
DEVICETYPE_GENERATOR = 0x00000002
DEVICETYPE_I2CHOST = 0x00000004
DEVICETYPE_COUNT = 3

IDKIND_PRODUCTID = 0x00000001
IDKIND_INDEX = 0x00000002
IDKIND_SERIALNUMBER = 0x00000004
IDKIND_COUNT = 3

STATUS_SUCCESS = 0
STATUS_VALUE_CLIPPED = 1
STATUS_VALUE_MODIFIED = 2
STATUS_UNSUCCESSFUL = -1
STATUS_NOT_SUPPORTED = -2
STATUS_INVALID_HANDLE = -3
STATUS_INVALID_VALUE = -4
STATUS_INVALID_CHANNEL = -5
STATUS_INVALID_TRIGGER_SOURCE = -6
STATUS_INVALID_DEVICE_TYPE = -7
STATUS_INVALID_DEVICE_INDEX = -8
STATUS_INVALID_PRODUCT_ID = -9
STATUS_INVALID_DEVICE_SERIALNUMBER = -10
STATUS_OBJECT_GONE = -11
STATUS_DEVICE_GONE = STATUS_OBJECT_GONE
STATUS_INTERNAL_ADDRESS = -12
STATUS_NOT_CONTROLLABLE = -13
STATUS_BIT_ERROR = -14
STATUS_NO_ACKNOWLEDGE = -15
STATUS_INVALID_CONTAINED_DEVICE_SERIALNUMBER = -16
STATUS_INVALID_INPUT = -17
STATUS_INVALID_OUTPUT = -18
STATUS_INVALID_DRIVER = -19
STATUS_NOT_AVAILABLE = -20
STATUS_INVALID_FIRMWARE = -21
STATUS_INVALID_INDEX = -22
STATUS_INVALID_EEPROM = -23
STATUS_INITIALIZATION_FAILED = -24
STATUS_LIBRARY_NOT_INITIALIZED = -25
STATUS_NO_TRIGGER_ENABLED = -26
STATUS_SYNCHRONIZATION_FAILED = -29
STATUS_INVALID_HS56_COMBINED_DEVICE = -30
STATUS_MEASUREMENT_RUNNING = -31

CONNECTORTYPE_UNKNOWN = 0x00000000
CONNECTORTYPE_BNC = 0x00000001
CONNECTORTYPE_BANANA = 0x00000002
CONNECTORTYPE_POWERPLUG = 0x00000004
CONNECTORTYPE_COUNT = 3
CONNECTORTYPE_MASK = (CONNECTORTYPE_BNC | CONNECTORTYPE_BANANA | CONNECTORTYPE_POWERPLUG)

DATARAWTYPE_UNKNOWN = 0x00000000
DATARAWTYPE_INT8 = 0x00000001
DATARAWTYPE_INT16 = 0x00000002
DATARAWTYPE_INT32 = 0x00000004
DATARAWTYPE_INT64 = 0x00000008
DATARAWTYPE_UINT8 = 0x00000010
DATARAWTYPE_UINT16 = 0x00000020
DATARAWTYPE_UINT32 = 0x00000040
DATARAWTYPE_UINT64 = 0x00000080
DATARAWTYPE_FLOAT32 = 0x00000100
DATARAWTYPE_FLOAT64 = 0x00000200
DATARAWTYPE_COUNT = 10
DATARAWTYPE_MASK_INT = (DATARAWTYPE_INT8 | DATARAWTYPE_INT16 | DATARAWTYPE_INT32 | DATARAWTYPE_INT64)
DATARAWTYPE_MASK_UINT = (DATARAWTYPE_UINT8 | DATARAWTYPE_UINT16 | DATARAWTYPE_UINT32 | DATARAWTYPE_UINT64)
DATARAWTYPE_MASK_FLOAT = (DATARAWTYPE_FLOAT32 | DATARAWTYPE_FLOAT64)
DATARAWTYPE_MASK_FIXED = (DATARAWTYPE_MASK_INT | DATARAWTYPE_MASK_UINT)

BOOL8_FALSE = 0
BOOL8_TRUE = 1

TRISTATE_UNDEFINED = 0
TRISTATE_FALSE = 1
TRISTATE_TRUE = 2

TRIGGERIO_INDEX_INVALID = 0xffff

STRING_LENGTH_NULL_TERMINATED = 0xffffffff

RANGEINDEX_AUTO = 0xffffffff

POINTER_ARRAY_MAX_LENGTH = 256

ARN_COUNT = 3

ARB_DISABLED = 0
ARB_NATIVEONLY = 1
ARB_ALL = 2

AR_UNKNOWN = 0
AR_DISABLED = (1 << ARB_DISABLED)
AR_NATIVEONLY = (1 << ARB_NATIVEONLY)
AR_ALL = (1 << ARB_ALL)

ARM_NONE = 0
ARM_ALL = ((1 << ARN_COUNT) - 1)
ARM_ENABLED = (ARM_ALL & ~AR_DISABLED)

CKN_COUNT = 5

CKB_DCV = 0
CKB_ACV = 1
CKB_DCA = 2
CKB_ACA = 3
CKB_OHM = 4

CK_UNKNOWN = 0
CK_DCV = (1 << CKB_DCV)
CK_ACV = (1 << CKB_ACV)
CK_DCA = (1 << CKB_DCA)
CK_ACA = (1 << CKB_ACA)
CK_OHM = (1 << CKB_OHM)

CKM_NONE = 0
CKM_V = (CK_DCV | CK_ACV)
CKM_A = (CK_DCA | CK_ACA)
CKM_OHM = (CK_OHM)
CKM_ASYMMETRICRANGE = (CKM_OHM)
CKM_SYMMETRICRANGE = (CKM_V | CKM_A)

CON_COUNT = 3

COB_DISABLED = 0
COB_SAMPLE = 1
COB_FIXED = 2

CO_DISABLED = (1 << COB_DISABLED)
CO_SAMPLE = (1 << COB_SAMPLE)
CO_FIXED = (1 << COB_FIXED)

COM_NONE = 0
COM_ALL = ((1 << CON_COUNT) - 1)
COM_ENABLED = (COM_ALL & ~CO_DISABLED)
COM_FREQUENCY = (CO_FIXED)

CSN_COUNT = 2

CSB_EXTERNAL = 0
CSB_INTERNAL = 1

CS_EXTERNAL = (1 << CSB_EXTERNAL)
CS_INTERNAL = (1 << CSB_INTERNAL)

CSM_NONE = 0
CSM_ALL = ((1 << CSN_COUNT) - 1)
CSM_FREQUENCY = (CS_EXTERNAL)

FMN_COUNT = 2

FMB_SIGNALFREQUENCY = 0
FMB_SAMPLEFREQUENCY = 1

FM_UNKNOWN = 0x00000000
FM_SIGNALFREQUENCY = (1 << FMB_SIGNALFREQUENCY)
FM_SAMPLEFREQUENCY = (1 << FMB_SAMPLEFREQUENCY)

FMM_NONE = 0x00000000
FMM_ALL = ((1 << FMN_COUNT) - 1)

GMN_COUNT = 12

GMB_CONTINUOUS = 0
GMB_BURST_COUNT = 1
GMB_GATED_PERIODS = 2
GMB_GATED = 3
GMB_GATED_PERIOD_START = 4
GMB_GATED_PERIOD_FINISH = 5
GMB_GATED_RUN = 6
GMB_GATED_RUN_OUTPUT = 7
GMB_BURST_SAMPLE_COUNT = 8
GMB_BURST_SAMPLE_COUNT_OUTPUT = 9
GMB_BURST_SEGMENT_COUNT = 10
GMB_BURST_SEGMENT_COUNT_OUTPUT = 11

GM_UNKNOWN = 0
GM_CONTINUOUS = (1 << GMB_CONTINUOUS)
GM_BURST_COUNT = (1 << GMB_BURST_COUNT)
GM_GATED_PERIODS = (1 << GMB_GATED_PERIODS)
GM_GATED = (1 << GMB_GATED)
GM_GATED_PERIOD_START = (1 << GMB_GATED_PERIOD_START)
GM_GATED_PERIOD_FINISH = (1 << GMB_GATED_PERIOD_FINISH)
GM_GATED_RUN = (1 << GMB_GATED_RUN)
GM_GATED_RUN_OUTPUT = (1 << GMB_GATED_RUN_OUTPUT)
GM_BURST_SAMPLE_COUNT = (1 << GMB_BURST_SAMPLE_COUNT)
GM_BURST_SAMPLE_COUNT_OUTPUT = (1 << GMB_BURST_SAMPLE_COUNT_OUTPUT)
GM_BURST_SEGMENT_COUNT = (1 << GMB_BURST_SEGMENT_COUNT)
GM_BURST_SEGMENT_COUNT_OUTPUT = (1 << GMB_BURST_SEGMENT_COUNT_OUTPUT)

GMM_NONE = 0
GMM_BURST_COUNT = (GM_BURST_COUNT)
GMM_GATED = (GM_GATED_PERIODS | GM_GATED | GM_GATED_PERIOD_START | GM_GATED_PERIOD_FINISH | GM_GATED_RUN | GM_GATED_RUN_OUTPUT)
GMM_BURST_SAMPLE_COUNT = (GM_BURST_SAMPLE_COUNT | GM_BURST_SAMPLE_COUNT_OUTPUT)
GMM_BURST_SEGMENT_COUNT = (GM_BURST_SEGMENT_COUNT | GM_BURST_SEGMENT_COUNT_OUTPUT)
GMM_BURST = (GMM_BURST_COUNT | GMM_BURST_SAMPLE_COUNT | GMM_BURST_SEGMENT_COUNT)
GMM_REQUIRE_TRIGGER = (GMM_GATED | GMM_BURST_SAMPLE_COUNT | GMM_BURST_SEGMENT_COUNT)
GMM_ALL = ((1 << GMN_COUNT) - 1)
GMM_SIGNALFREQUENCY = (GMM_ALL & ~GMM_BURST_SAMPLE_COUNT)
GMM_SAMPLEFREQUENCY = (GMM_ALL)
GMM_SINE = (GMM_SIGNALFREQUENCY)
GMM_TRIANGLE = (GMM_SIGNALFREQUENCY)
GMM_SQUARE = (GMM_SIGNALFREQUENCY)
GMM_DC = (GM_CONTINUOUS)
GMM_NOISE = (GM_CONTINUOUS | GM_GATED)
GMM_ARBITRARY = (GMM_SIGNALFREQUENCY | GMM_SAMPLEFREQUENCY)
GMM_PULSE = (GMM_SIGNALFREQUENCY & ~GMM_BURST_SEGMENT_COUNT)

GSN_COUNT = 4

GSB_STOPPED = 0
GSB_RUNNING = 1
GSB_BURSTACTIVE = 2
GSB_WAITING = 3

GS_STOPPED = (1 << GSB_STOPPED)
GS_RUNNING = (1 << GSB_RUNNING)
GS_BURSTACTIVE = (1 << GSB_BURSTACTIVE)
GS_WAITING = (1 << GSB_WAITING)

GSM_NONE = 0
GSM_ALL = ((1 << GSN_COUNT) - 1)

MMN_COUNT = 2

MMB_STREAM = 0
MMB_BLOCK = 1

MMM_NONE = 0
MMM_ALL = ((1 << MMN_COUNT) - 1)

MM_UNKNOWN = 0
MM_STREAM = (1 << MMB_STREAM)
MM_BLOCK = (1 << MMB_BLOCK)

STN_COUNT = 7

STB_SINE = 0
STB_TRIANGLE = 1
STB_SQUARE = 2
STB_DC = 3
STB_NOISE = 4
STB_ARBITRARY = 5
STB_PULSE = 6

ST_UNKNOWN = 0
ST_SINE = (1 << STB_SINE)
ST_TRIANGLE = (1 << STB_TRIANGLE)
ST_SQUARE = (1 << STB_SQUARE)
ST_DC = (1 << STB_DC)
ST_NOISE = (1 << STB_NOISE)
ST_ARBITRARY = (1 << STB_ARBITRARY)
ST_PULSE = (1 << STB_PULSE)

STM_NONE = 0
STM_AMPLITUDE = (ST_SINE | ST_TRIANGLE | ST_SQUARE | ST_NOISE | ST_ARBITRARY | ST_PULSE)
STM_OFFSET = (ST_SINE | ST_TRIANGLE | ST_SQUARE | ST_DC | ST_NOISE | ST_ARBITRARY | ST_PULSE)
STM_FREQUENCY = (ST_SINE | ST_TRIANGLE | ST_SQUARE | ST_NOISE | ST_ARBITRARY | ST_PULSE)
STM_PHASE = (ST_SINE | ST_TRIANGLE | ST_SQUARE | ST_ARBITRARY | ST_PULSE)
STM_SYMMETRY = (ST_SINE | ST_TRIANGLE | ST_SQUARE)
STM_WIDTH = (ST_PULSE)
STM_LEADINGEDGETIME = (ST_PULSE)
STM_TRAILINGEDGETIME = (ST_PULSE)
STM_DATALENGTH = (ST_ARBITRARY)
STM_DATA = (ST_ARBITRARY)
STM_EDGETIME = (STM_LEADINGEDGETIME & STM_TRAILINGEDGETIME)

TCN_COUNT = 5

TCB_NONE = 0
TCB_SMALLER = 1
TCB_LARGER = 2
TCB_INSIDE = 3
TCB_OUTSIDE = 4

TC_UNKNOWN = 0
TC_NONE = (1 << TCB_NONE)
TC_SMALLER = (1 << TCB_SMALLER)
TC_LARGER = (1 << TCB_LARGER)
TC_INSIDE = (1 << TCB_INSIDE)
TC_OUTSIDE = (1 << TCB_OUTSIDE)

TCM_NONE = 0
TCM_ALL = ((1 << TCN_COUNT) - 1)
TCM_ENABLED = (TCM_ALL & ~TC_NONE)

TH_ALLPRESAMPLES = 0xffffffffffffffff

DN_MAIN = 0
DN_SUB_FIRST = 1
DN_SUB_SECOND = 2

PGID_OSCILLOSCOPE = 1
PGID_GENERATOR = 2
PGID_EXTERNAL_DSUB = 3

SGID_MAIN = 0
SGID_CHANNEL1 = 1
SGID_CHANNEL2 = 2
SGID_PIN1 = 1
SGID_PIN2 = 2
SGID_PIN3 = 3

FID_SCP_TRIGGERED = 0
FID_GEN_START = 0
FID_GEN_STOP = 1
FID_GEN_NEW_PERIOD = 2
FID_EXT_TRIGGERED = 0

TIOID_SHIFT_PGID = 20
TIOID_SHIFT_DN = 24
TIOID_SHIFT_SGID = 8
TIOID_SHIFT_FID = 0

TIID_INVALID = 0
TIID_EXT1 = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_EXTERNAL_DSUB) << TIOID_SHIFT_PGID) | ((SGID_PIN1) << TIOID_SHIFT_SGID) | ((FID_EXT_TRIGGERED) << TIOID_SHIFT_FID))
TIID_EXT2 = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_EXTERNAL_DSUB) << TIOID_SHIFT_PGID) | ((SGID_PIN2) << TIOID_SHIFT_SGID) | ((FID_EXT_TRIGGERED) << TIOID_SHIFT_FID))
TIID_EXT3 = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_EXTERNAL_DSUB) << TIOID_SHIFT_PGID) | ((SGID_PIN3) << TIOID_SHIFT_SGID) | ((FID_EXT_TRIGGERED) << TIOID_SHIFT_FID))
TIID_GENERATOR_START = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_GENERATOR) << TIOID_SHIFT_PGID) | ((SGID_MAIN) << TIOID_SHIFT_SGID) | ((FID_GEN_START) << TIOID_SHIFT_FID))
TIID_GENERATOR_STOP = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_GENERATOR) << TIOID_SHIFT_PGID) | ((SGID_MAIN) << TIOID_SHIFT_SGID) | ((FID_GEN_STOP) << TIOID_SHIFT_FID))
TIID_GENERATOR_NEW_PERIOD = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_GENERATOR) << TIOID_SHIFT_PGID) | ((SGID_MAIN) << TIOID_SHIFT_SGID) | ((FID_GEN_NEW_PERIOD) << TIOID_SHIFT_FID))

TOID_INVALID = 0
TOID_EXT1 = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_EXTERNAL_DSUB) << TIOID_SHIFT_PGID) | ((SGID_PIN1) << TIOID_SHIFT_SGID) | ((FID_EXT_TRIGGERED) << TIOID_SHIFT_FID))
TOID_EXT2 = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_EXTERNAL_DSUB) << TIOID_SHIFT_PGID) | ((SGID_PIN2) << TIOID_SHIFT_SGID) | ((FID_EXT_TRIGGERED) << TIOID_SHIFT_FID))
TOID_EXT3 = ((DN_MAIN << TIOID_SHIFT_DN) | ((PGID_EXTERNAL_DSUB) << TIOID_SHIFT_PGID) | ((SGID_PIN3) << TIOID_SHIFT_SGID) | ((FID_EXT_TRIGGERED) << TIOID_SHIFT_FID))

TKN_COUNT = 13

TKB_RISINGEDGE = 0
TKB_FALLINGEDGE = 1
TKB_INWINDOW = 2
TKB_OUTWINDOW = 3
TKB_ANYEDGE = 4
TKB_ENTERWINDOW = 5
TKB_EXITWINDOW = 6
TKB_PULSEWIDTHPOSITIVE = 7
TKB_PULSEWIDTHNEGATIVE = 8
TKB_PULSEWIDTHEITHER = 9
TKB_RUNTPULSEPOSITIVE = 10
TKB_RUNTPULSENEGATIVE = 11
TKB_RUNTPULSEEITHER = 12

TK_UNKNOWN = 0
TK_RISINGEDGE = (1 << TKB_RISINGEDGE)
TK_FALLINGEDGE = (1 << TKB_FALLINGEDGE)
TK_INWINDOW = (1 << TKB_INWINDOW)
TK_OUTWINDOW = (1 << TKB_OUTWINDOW)
TK_ANYEDGE = (1 << TKB_ANYEDGE)
TK_ENTERWINDOW = (1 << TKB_ENTERWINDOW)
TK_EXITWINDOW = (1 << TKB_EXITWINDOW)
TK_PULSEWIDTHPOSITIVE = (1 << TKB_PULSEWIDTHPOSITIVE)
TK_PULSEWIDTHNEGATIVE = (1 << TKB_PULSEWIDTHNEGATIVE)
TK_PULSEWIDTHEITHER = (1 << TKB_PULSEWIDTHEITHER)
TK_RUNTPULSEPOSITIVE = (1 << TKB_RUNTPULSEPOSITIVE)
TK_RUNTPULSENEGATIVE = (1 << TKB_RUNTPULSENEGATIVE)
TK_RUNTPULSEEITHER = (1 << TKB_RUNTPULSEEITHER)

TKM_NONE = 0
TKM_EDGE = (TK_RISINGEDGE | TK_FALLINGEDGE | TK_ANYEDGE)
TKM_WINDOW = (TK_INWINDOW | TK_OUTWINDOW | TK_ENTERWINDOW | TK_EXITWINDOW)
TKM_PULSEWIDTH = (TK_PULSEWIDTHPOSITIVE | TK_PULSEWIDTHNEGATIVE | TK_PULSEWIDTHEITHER)
TKM_RUNTPULSE = (TK_RUNTPULSEPOSITIVE | TK_RUNTPULSENEGATIVE | TK_RUNTPULSEEITHER)
TKM_PULSE = (TKM_PULSEWIDTH | TKM_RUNTPULSE)
TKM_TIME = (TKM_PULSEWIDTH | TKM_WINDOW)
TKM_ALL = ((1 << TKN_COUNT) - 1)

TLMN_COUNT = 2

TLMB_RELATIVE = 0
TLMB_ABSOLUTE = 1

TLM_UNKNOWN = 0
TLM_RELATIVE = (1 << TLMB_RELATIVE)
TLM_ABSOLUTE = (1 << TLMB_ABSOLUTE)

TLMM_NONE = 0
TLMM_ALL = ((1 << TLMN_COUNT) - 1)

TO_INFINITY = -1

TOEN_COUNT = 6

TOEB_GENERATOR_START = 0
TOEB_GENERATOR_STOP = 1
TOEB_GENERATOR_NEWPERIOD = 2
TOEB_OSCILLOSCOPE_RUNNING = 3
TOEB_OSCILLOSCOPE_TRIGGERED = 4
TOEB_MANUAL = 5

TOE_UNKNOWN = 0
TOE_GENERATOR_START = (1 << TOEB_GENERATOR_START)
TOE_GENERATOR_STOP = (1 << TOEB_GENERATOR_STOP)
TOE_GENERATOR_NEWPERIOD = (1 << TOEB_GENERATOR_NEWPERIOD)
TOE_OSCILLOSCOPE_RUNNING = (1 << TOEB_OSCILLOSCOPE_RUNNING)
TOE_OSCILLOSCOPE_TRIGGERED = (1 << TOEB_OSCILLOSCOPE_TRIGGERED)
TOE_MANUAL = (1 << TOEB_MANUAL)

TOEM_NONE = 0
TOEM_GENERATOR = (TOE_GENERATOR_START | TOE_GENERATOR_STOP | TOE_GENERATOR_NEWPERIOD)
TOEM_OSCILLOSCOPE = (TOE_OSCILLOSCOPE_RUNNING | TOE_OSCILLOSCOPE_TRIGGERED)
TOEM_ALL = ((1 << TOEN_COUNT) - 1)

PID_NONE = 0
PID_COMBI = 2
PID_HS3 = 13
PID_HS4 = 15
PID_HP3 = 18
PID_TP450 = 19
PID_HS4D = 20
PID_HS5 = 22
PID_HS6D = 25
PID_ATS610004D = 31
PID_ATS605004D = 32

EVENTID_INVALID = 0
EVENTID_OBJ_REMOVED = 1
EVENTID_SCP_DATAREADY = 2
EVENTID_SCP_DATAOVERFLOW = 3
EVENTID_SCP_CONNECTIONTESTCOMPLETED = 4
EVENTID_SCP_TRIGGERED = 5
EVENTID_GEN_BURSTCOMPLETED = 6
EVENTID_GEN_CONTROLLABLECHANGED = 7
EVENTID_SRV_STATUSCHANGED = 8
EVENTID_SCP_SAFEGROUNDERROR = 9
EVENTID_SCP_GETDATAASYNCCOMPLETED = 10

if platform.system() == 'Windows':
    WM_USER = 0x0400
    WM_LIBTIEPIE = (WM_USER + 1337)
    WM_LIBTIEPIE_LST_DEVICEADDED = (WM_LIBTIEPIE + 2)
    WM_LIBTIEPIE_LST_DEVICEREMOVED = (WM_LIBTIEPIE + 3)
    WM_LIBTIEPIE_LST_DEVICECANOPENCHANGED = (WM_LIBTIEPIE + 9)
    WM_LIBTIEPIE_DEV_REMOVED = (WM_LIBTIEPIE + 4)
    WM_LIBTIEPIE_SCP_DATAREADY = (WM_LIBTIEPIE + 0)
    WM_LIBTIEPIE_SCP_DATAOVERFLOW = (WM_LIBTIEPIE + 1)
    WM_LIBTIEPIE_SCP_CONNECTIONTESTCOMPLETED = (WM_LIBTIEPIE + 7)
    WM_LIBTIEPIE_SCP_TRIGGERED = (WM_LIBTIEPIE + 8)
    WM_LIBTIEPIE_GEN_BURSTCOMPLETED = (WM_LIBTIEPIE + 5)
    WM_LIBTIEPIE_GEN_CONTROLLABLECHANGED = (WM_LIBTIEPIE + 6)
    WM_LIBTIEPIE_EVENT = (WM_LIBTIEPIE + 10)

AUTO_RESOLUTION_MODES = {
    AR_UNKNOWN: 'Unknown',
    AR_DISABLED: 'Disabled',
    AR_NATIVEONLY: 'Native only',
    AR_ALL: 'All',
}

COUPLINGS = {
    CK_UNKNOWN: 'Unknown',
    CK_DCV: 'DCV',
    CK_ACV: 'ACV',
    CK_DCA: 'DCA',
    CK_ACA: 'ACA',
    CK_OHM: 'Ohm',
}

CLOCK_OUTPUTS = {
    CO_DISABLED: 'Disabled',
    CO_SAMPLE: 'Sample',
    CO_FIXED: 'Fixed',
}

CLOCK_SOURCES = {
    CS_EXTERNAL: 'External',
    CS_INTERNAL: 'Internal',
}

CONNECTOR_TYPES = {
    CONNECTORTYPE_UNKNOWN: 'Unknown',
    CONNECTORTYPE_BNC: 'BNC',
    CONNECTORTYPE_BANANA: 'Banana',
    CONNECTORTYPE_POWERPLUG: 'Power plug',
}

DEVICE_TYPES = {
    DEVICETYPE_OSCILLOSCOPE: 'Oscilloscope',
    DEVICETYPE_GENERATOR: 'Generator',
    DEVICETYPE_I2CHOST: 'I2CHost',
}

FREQUENCY_MODES = {
    FM_UNKNOWN: 'Unknown',
    FM_SIGNALFREQUENCY: 'Signal frequency',
    FM_SAMPLEFREQUENCY: 'Sample frequency',
}

GENERATOR_MODES = {
    GM_UNKNOWN: 'Unknown',
    GM_CONTINUOUS: 'Continuous',
    GM_BURST_COUNT: 'Burst count',
    GM_GATED_PERIODS: 'Gated periods',
    GM_GATED: 'Gated',
    GM_GATED_PERIOD_START: 'Gated period start',
    GM_GATED_PERIOD_FINISH: 'Gated period finish',
    GM_GATED_RUN: 'Gated run',
    GM_GATED_RUN_OUTPUT: 'Gated run output',
    GM_BURST_SAMPLE_COUNT: 'Burst sample count',
    GM_BURST_SAMPLE_COUNT_OUTPUT: 'Burst sample count output',
    GM_BURST_SEGMENT_COUNT: 'Burst segment count',
    GM_BURST_SEGMENT_COUNT_OUTPUT: 'Burst segment count output',
}

GENERATOR_STATUSS = {
    GS_STOPPED: 'Stopped',
    GS_RUNNING: 'Running',
    GS_BURSTACTIVE: 'Burst active',
    GS_WAITING: 'Waiting',
}

INTERFACES = {
    INTERFACE_DEVICE: 'Device',
    INTERFACE_OSCILLOSCOPE: 'Oscilloscope',
    INTERFACE_GENERATOR: 'Generator',
    INTERFACE_I2CHOST: 'I2CHost',
}

MEASURE_MODES = {
    MM_UNKNOWN: 'Unknown',
    MM_STREAM: 'Stream',
    MM_BLOCK: 'Block',
}

SIGNAL_TYPES = {
    ST_UNKNOWN: 'Unknown',
    ST_SINE: 'Sine',
    ST_TRIANGLE: 'Triangle',
    ST_SQUARE: 'Square',
    ST_DC: 'DC',
    ST_NOISE: 'Noise',
    ST_ARBITRARY: 'Arbitrary',
    ST_PULSE: 'Pulse',
}

TRIGGER_CONDITIONS = {
    TC_UNKNOWN: 'Unknown',
    TC_NONE: 'None',
    TC_SMALLER: 'Smaller',
    TC_LARGER: 'Larger',
    TC_INSIDE: 'Inside',
    TC_OUTSIDE: 'Outside',
}

TRIGGER_KINDS = {
    TK_UNKNOWN: 'Unknown',
    TK_RISINGEDGE: 'Rising edge',
    TK_FALLINGEDGE: 'Falling edge',
    TK_INWINDOW: 'In window',
    TK_OUTWINDOW: 'Out window',
    TK_ANYEDGE: 'Any edge',
    TK_ENTERWINDOW: 'Enter window',
    TK_EXITWINDOW: 'Exit window',
    TK_PULSEWIDTHPOSITIVE: 'Pulse width positive',
    TK_PULSEWIDTHNEGATIVE: 'Pulse width negative',
    TK_PULSEWIDTHEITHER: 'Pulse width either',
    TK_RUNTPULSEPOSITIVE: 'Runt pulse positive',
    TK_RUNTPULSENEGATIVE: 'Runt pulse negative',
    TK_RUNTPULSEEITHER: 'Runt pulse either',
}

TRIGGER_LEVEL_MODES = {
    TLM_UNKNOWN: 'Unknown',
    TLM_RELATIVE: 'Relative',
    TLM_ABSOLUTE: 'Absolute',
}

TRIGGER_OUTPUT_EVENTS = {
    TOE_UNKNOWN: 'Unknown',
    TOE_GENERATOR_START: 'Generator start',
    TOE_GENERATOR_STOP: 'Generator stop',
    TOE_GENERATOR_NEWPERIOD: 'Generator new period',
    TOE_OSCILLOSCOPE_RUNNING: 'Oscilloscope running',
    TOE_OSCILLOSCOPE_TRIGGERED: 'Oscilloscope triggered',
    TOE_MANUAL: 'Manual',
}