#!/usr/bin/env python3
# encoding: utf-8

import LibsCompiler.DLA
import LibsCompiler.Compile
import file_encoder
from LibsCompiler.head import headers as headers

# En Linux no causa conflicto la libreria NX
#file_encoder.init()

#code = LibsCompiler.DLA.Read().segment("DLA_ESCRITA_PRUEBA.dla", "clase_ejemplo", "HOLA")
#code = LibsCompiler.DLA.Read().block("ejemplo.dla", "clase_prueba", ORDER = ["SI", "YES", "PUEDE", "NO"])
#LibsCompiler.Compile.run(code)

LibsCompiler.DLA.Write("libreria de ejemplo.dlib", "clase_ejemplo", "HOLA")

#LibsCompiler.DLA.Write("libreria de ejemplo.dlib", "clase_test", "SI")
