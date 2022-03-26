#!/usr/bin/env python3
# encoding: utf-8

import LibsCompiler.DLA
import LibsCompiler.Compile
import file_encoder
from LibsCompiler.head import headers as headers

# En Linux no causa conflicto la libreria NX
#file_encoder.init()

code = LibsCompiler.DLA.Read().segment("saved.dla", "class_ESTES", "POS")

#LibsCompiler.DLA.Write("libreria de ejemplo_dos.dlib", "class_ESTE", "SI")

# -> # LibsCompiler.DLA.Write("libreria de ejemplo_dos.dlib", "class_prueba", "NUEVADOS")

#code = LibsCompiler.DLA.Read().block("saved.dla", "class_TESTES")

print(code)
LibsCompiler.Compile.run(code)
LibsCompiler.DLA.delete_cache()

#LibsCompiler.DLA.deconstruct("saved.dla")