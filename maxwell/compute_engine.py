from command_buffer import *
from nvgpu import GpuMemory
from maxwell.hw import *
from maxwell.hw.compute_b import *
from maxwell.hw.compute_b_qmd import *


def initialize_compute_engine(
    command_buffer: CommandBuffer,
    scratch_memory: GpuMemory,
    shader_program_memory: GpuMemory,
    bindless_texture_cbuff_index: int,
    sm_count: int,
):
    command_buffer.write_u32(
        InlineCommand(NVB1C0_SET_SHADER_EXCEPTIONS, SUBCHANNEL_ID_COMPUTE, 0)
    )

    command_buffer.write_u32(
        InlineCommand(
            NVB1C0_SET_BINDLESS_TEXTURE,
            SUBCHANNEL_ID_COMPUTE,
            bindless_texture_cbuff_index,
        )
    )

    command_buffer.write_u32(
        IncrCommand(NVB1C0_SET_SHADER_LOCAL_MEMORY_WINDOW, SUBCHANNEL_ID_COMPUTE, 1)
    )
    command_buffer.write_u32(0x1000000)

    command_buffer.write_u32(
        IncrCommand(NVB1C0_SET_SHADER_SHARED_MEMORY_WINDOW, SUBCHANNEL_ID_COMPUTE, 1)
    )
    command_buffer.write_u32(0x3000000)

    command_buffer.write_u32(
        IncrCommand(NVB1C0_SET_PROGRAM_REGION_A, SUBCHANNEL_ID_COMPUTE, 2)
    )
    command_buffer.write_u64(shader_program_memory.gpu_address)

    command_buffer.write_u32(
        InlineCommand(
            NVB1C0_SET_SPA_VERSION,
            SUBCHANNEL_ID_COMPUTE,
            NVB1C0_SET_SPA_VERSION_MAJOR(5) | NVB1C0_SET_SPA_VERSION_MAJOR(3),
        )
    )

    command_buffer.write_u32(
        IncrCommand(NVB1C0_SET_SHADER_LOCAL_MEMORY_A, SUBCHANNEL_ID_COMPUTE, 2)
    )
    command_buffer.write_u64(scratch_memory.gpu_address)

    scratch_memory_per_sm = scratch_memory.gpu_memory_size // sm_count
    command_buffer.write_u32(
        IncrCommand(
            NVB1C0_SET_SHADER_LOCAL_MEMORY_NON_THROTTLED_A, SUBCHANNEL_ID_COMPUTE, 6
        )
    )
    command_buffer.write_u32(0)
    command_buffer.write_u32(scratch_memory_per_sm)
    command_buffer.write_u32(0x100)
    command_buffer.write_u32(0)
    command_buffer.write_u32(scratch_memory_per_sm)
    command_buffer.write_u32(0x100)


def memcpy_inline_host_to_device(
    command_buffer: CommandBuffer, dest_address: int, data: bytes
):
    buffer = bytearray(data)

    while len(buffer) % 4 != 0:
        buffer += bytearray(b"\x00")

    command_buffer.write_u32(
        IncrCommand(NVB1C0_LINE_LENGTH_IN, SUBCHANNEL_ID_COMPUTE, 4)
    )
    command_buffer.write_u32(len(data))
    command_buffer.write_u32(1)
    command_buffer.write_u64(dest_address)

    command_buffer.write_u32(IncrCommand(NVB1C0_LAUNCH_DMA, SUBCHANNEL_ID_COMPUTE, 1))

    launch_dma_value = NVB1C0_LAUNCH_DMA_DST_MEMORY_LAYOUT(
        NVB1C0_LAUNCH_DMA_DST_MEMORY_LAYOUT_PITCH
    ) | NVB1C0_LAUNCH_DMA_COMPLETION_TYPE(NVB1C0_LAUNCH_DMA_COMPLETION_TYPE_FLUSH_ONLY)

    command_buffer.write_u32(launch_dma_value)

    command_buffer.write_u32(
        NonIncrCommand(NVB1C0_LOAD_INLINE_DATA, SUBCHANNEL_ID_COMPUTE, len(buffer) // 4)
    )
    command_buffer.write_bytes(buffer)
