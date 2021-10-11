#!/usr/bin/env python3
# encoding: utf-8

import LibsCompiler.DLA
import LibsCompiler.Compile
import file_encoder

# En Linux no causa conflicto la libreria NX
#file_encoder.init()

code = LibsCompiler.DLA.read().segment("ejemplo.dla", "class_test", "TE")
LibsCompiler.Compile.run(code)
