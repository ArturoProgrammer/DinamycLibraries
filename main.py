#!/usr/bin/env python3
# encoding: utf-8

import LibsCompiler.DLA
import LibsCompiler.Compile
import file_encoder
from LibsCompiler.head import headers as headers

# En Linux no causa conflicto la libreria NX
#file_encoder.init()

#code = LibsCompiler.DLA.read().segment("ejemplo.dla", "clase_prueba", "SI")
code = LibsCompiler.DLA.read().block("ejemplo.dla", "clase_prueba", ORDER = ["SI", "YES", "PUEDE", "NO"])
LibsCompiler.Compile.run(code)
