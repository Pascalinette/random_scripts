# AUTOGENERATED: DO NOT EDIT
# Last update date: 2022-02-04 16:15:59.250784

from ctypes import *


MAXWELL_CHANNEL_GPFIFO_A: int = 0xB06F
NVB06F_NUMBER_OF_SUBCHANNELS: int = 0x8
NVB06F_SET_OBJECT: int = 0x0
NVB06F_SET_OBJECT_ENGINE_SW: int = 0x1F
NVB06F_ILLEGAL: int = 0x4
NVB06F_NOP: int = 0x8
NVB06F_SEMAPHOREA: int = 0x10
NVB06F_SEMAPHOREB: int = 0x14
NVB06F_SEMAPHOREC: int = 0x18
NVB06F_SEMAPHORED: int = 0x1C
NVB06F_SEMAPHORED_OPERATION_ACQUIRE: int = 0x1
NVB06F_SEMAPHORED_OPERATION_RELEASE: int = 0x2
NVB06F_SEMAPHORED_OPERATION_ACQ_GEQ: int = 0x4
NVB06F_SEMAPHORED_OPERATION_ACQ_AND: int = 0x8
NVB06F_SEMAPHORED_OPERATION_REDUCTION: int = 0x10
NVB06F_SEMAPHORED_ACQUIRE_SWITCH_DISABLED: int = 0x0
NVB06F_SEMAPHORED_ACQUIRE_SWITCH_ENABLED: int = 0x1
NVB06F_SEMAPHORED_RELEASE_WFI_EN: int = 0x0
NVB06F_SEMAPHORED_RELEASE_WFI_DIS: int = 0x1
NVB06F_SEMAPHORED_RELEASE_SIZE_16BYTE: int = 0x0
NVB06F_SEMAPHORED_RELEASE_SIZE_4BYTE: int = 0x1
NVB06F_SEMAPHORED_REDUCTION_MIN: int = 0x0
NVB06F_SEMAPHORED_REDUCTION_MAX: int = 0x1
NVB06F_SEMAPHORED_REDUCTION_XOR: int = 0x2
NVB06F_SEMAPHORED_REDUCTION_AND: int = 0x3
NVB06F_SEMAPHORED_REDUCTION_OR: int = 0x4
NVB06F_SEMAPHORED_REDUCTION_ADD: int = 0x5
NVB06F_SEMAPHORED_REDUCTION_INC: int = 0x6
NVB06F_SEMAPHORED_REDUCTION_DEC: int = 0x7
NVB06F_SEMAPHORED_FORMAT_SIGNED: int = 0x0
NVB06F_SEMAPHORED_FORMAT_UNSIGNED: int = 0x1
NVB06F_NON_STALL_INTERRUPT: int = 0x20
NVB06F_FB_FLUSH: int = 0x24
NVB06F_MEM_OP_C: int = 0x30
NVB06F_MEM_OP_C_TLB_INVALIDATE_PDB_ONE: int = 0x0
NVB06F_MEM_OP_C_TLB_INVALIDATE_PDB_ALL: int = 0x1
NVB06F_MEM_OP_C_TLB_INVALIDATE_GPC_ENABLE: int = 0x0
NVB06F_MEM_OP_C_TLB_INVALIDATE_GPC_DISABLE: int = 0x1
NVB06F_MEM_OP_C_TLB_INVALIDATE_TARGET_VID_MEM: int = 0x0
NVB06F_MEM_OP_C_TLB_INVALIDATE_TARGET_SYS_MEM_COHERENT: int = 0x2
NVB06F_MEM_OP_C_TLB_INVALIDATE_TARGET_SYS_MEM_NONCOHERENT: int = 0x3
NVB06F_MEM_OP_D: int = 0x34
NVB06F_MEM_OP_D_OPERATION_MEMBAR: int = 0x5
NVB06F_MEM_OP_D_OPERATION_MMU_TLB_INVALIDATE: int = 0x9
NVB06F_MEM_OP_D_OPERATION_L2_PEERMEM_INVALIDATE: int = 0xD
NVB06F_MEM_OP_D_OPERATION_L2_SYSMEM_INVALIDATE: int = 0xE
NVB06F_MEM_OP_D_OPERATION_L2_CLEAN_COMPTAGS: int = 0xF
NVB06F_MEM_OP_D_OPERATION_L2_FLUSH_DIRTY: int = 0x10
NVB06F_SET_REFERENCE: int = 0x50
NVB06F_WFI: int = 0x78
NVB06F_WFI_SCOPE_CURRENT_SCG_TYPE: int = 0x0
NVB06F_WFI_SCOPE_ALL: int = 0x1
NVB06F_CRC_CHECK: int = 0x7C
NVB06F_YIELD: int = 0x80
NVB06F_YIELD_OP_NOP: int = 0x0
NVB06F_YIELD_OP_PBDMA_TIMESLICE: int = 0x1
NVB06F_YIELD_OP_RUNLIST_TIMESLICE: int = 0x2
NVB06F_YIELD_OP_TSG: int = 0x3
NVB06F_GP_ENTRY__SIZE: int = 0x8
NVB06F_GP_ENTRY0_FETCH_UNCONDITIONAL: int = 0x0
NVB06F_GP_ENTRY0_FETCH_CONDITIONAL: int = 0x1
NVB06F_GP_ENTRY1_PRIV_USER: int = 0x0
NVB06F_GP_ENTRY1_PRIV_KERNEL: int = 0x1
NVB06F_GP_ENTRY1_LEVEL_MAIN: int = 0x0
NVB06F_GP_ENTRY1_LEVEL_SUBROUTINE: int = 0x1
NVB06F_GP_ENTRY1_SYNC_PROCEED: int = 0x0
NVB06F_GP_ENTRY1_SYNC_WAIT: int = 0x1
NVB06F_GP_ENTRY1_OPCODE_NOP: int = 0x0
NVB06F_GP_ENTRY1_OPCODE_ILLEGAL: int = 0x1
NVB06F_GP_ENTRY1_OPCODE_GP_CRC: int = 0x2
NVB06F_GP_ENTRY1_OPCODE_PB_CRC: int = 0x3
NVB06F_DMA_TERT_OP_GRP0_INC_METHOD: int = 0x0
NVB06F_DMA_TERT_OP_GRP0_SET_SUB_DEV_MASK: int = 0x1
NVB06F_DMA_TERT_OP_GRP0_STORE_SUB_DEV_MASK: int = 0x2
NVB06F_DMA_TERT_OP_GRP0_USE_SUB_DEV_MASK: int = 0x3
NVB06F_DMA_TERT_OP_GRP2_NON_INC_METHOD: int = 0x0
NVB06F_DMA_SEC_OP_GRP0_USE_TERT: int = 0x0
NVB06F_DMA_SEC_OP_INC_METHOD: int = 0x1
NVB06F_DMA_SEC_OP_GRP2_USE_TERT: int = 0x2
NVB06F_DMA_SEC_OP_NON_INC_METHOD: int = 0x3
NVB06F_DMA_SEC_OP_IMMD_DATA_METHOD: int = 0x4
NVB06F_DMA_SEC_OP_ONE_INC: int = 0x5
NVB06F_DMA_SEC_OP_RESERVED6: int = 0x6
NVB06F_DMA_SEC_OP_END_PB_SEGMENT: int = 0x7
NVB06F_DMA_INCR_OPCODE_VALUE: int = 0x1
NVB06F_DMA_NONINCR_OPCODE_VALUE: int = 0x3
NVB06F_DMA_ONEINCR_OPCODE_VALUE: int = 0x5
NVB06F_DMA_NOP: int = 0x0
NVB06F_DMA_IMMD_OPCODE_VALUE: int = 0x4
NVB06F_DMA_SET_SUBDEVICE_MASK_OPCODE_VALUE: int = 0x1
NVB06F_DMA_STORE_SUBDEVICE_MASK_OPCODE_VALUE: int = 0x2
NVB06F_DMA_USE_SUBDEVICE_MASK_OPCODE_VALUE: int = 0x3
NVB06F_DMA_ENDSEG_OPCODE_VALUE: int = 0x7
NVB06F_DMA_OPCODE3_NONE: int = 0x0
NVB06F_DMA_OPCODE_METHOD: int = 0x0
NVB06F_DMA_OPCODE_NONINC_METHOD: int = 0x2


class _clb06f_tag0(Structure):
    _fields_ = [
        ("Ignored00", c_int * 16),
        ("Put", c_int),
        ("Get", c_int),
        ("Reference", c_int),
        ("PutHi", c_int),
        ("Ignored01", c_int * 2),
        ("TopLevelGet", c_int),
        ("TopLevelGetHi", c_int),
        ("GetHi", c_int),
        ("Ignored02", c_int * 7),
        ("Ignored03", c_int),
        ("Ignored04", c_int * 1),
        ("GPGet", c_int),
        ("GPPut", c_int),
        ("Ignored05", c_int * 92),
    ]




