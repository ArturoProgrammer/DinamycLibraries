#!/usr/bin/env python3
# encoding: utf-8

import LibsCompiler.DLA
import LibsCompiler.Compile
import file_encoder
from LibsCompiler.head import headers as headers

# En Linux no causa conflicto la libreria NX
#file_encoder.init()


#LibsCompiler.DLA.Write("saved.dlib", "class_ESTESSSS", "YESSS")

LibsCompiler.DLA.Write("ejemplo.dlib", "clase_prueba", "NO")
code = LibsCompiler.DLA.Read().segment("ejemplo.dla", "clase_prueba", "NO")

#code = LibsCompiler.DLA.Read().block("saved.dla", "class_TESTES", ORDER = ["POS", "POST"])

print(code)
LibsCompiler.Compile.run(code)
LibsCompiler.DLA.delete_cache()

#LibsCompiler.DLA.deconstruct("saved.dla")