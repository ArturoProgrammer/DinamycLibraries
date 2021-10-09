"""
import libsCompilerx86
import file_encoder


file_encoder.init()

if __name__ == '__main__':
    libsCompilerx86.DLACodeFile().readSegmentCode("ejemplo.dla", "class_test", "OS")
"""

import LibsCompiler.DLA
import LibsCompiler.Compile
import file_encoder

file_encoder.init()

if __name__ == '__main__':
	val = LibsCompiler.DLA.read().segment("ejemplo.dla", "class_test", "TE")
	LibsCompiler.Compile.run(val)