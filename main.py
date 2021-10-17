#!/usr/bin/env python3
# encoding: utf-8

import LibsCompiler.DLA
import LibsCompiler.Compile
import file_encoder
from LibsCompiler.head import headers as headers

# En Linux no causa conflicto la libreria NX
#file_encoder.init()

code = LibsCompiler.DLA.read().segment("ejemplo.dla", "clase_test", "SI")
LibsCompiler.Compile.run(code)
