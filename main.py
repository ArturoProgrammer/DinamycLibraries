#!/usr/bin/env python3
# encoding: utf-8

import LibsCompiler.DLA
import LibsCompiler.Compile
import file_encoder
from LibsCompiler.head import headers as headers
import prompt

# En Linux no causa conflicto la libreria NX
#file_encoder.init()


#LibsCompiler.DLA.Write("saved.dlib", "class_ESTESSSS", "YESSS")


#LibsCompiler.DLA.Write("ejemplo.dlib", "class_prueba", "NO")

#code = LibsCompiler.DLA.Read().segment("ejemplo.dla", "class_prueba", "NO")
"""
code = LibsCompiler.DLA.Read().block("ejemplo.dla", "class_prueba", ORDER = ["NO"])
"""

#print(code)


prompt.cin("WRITE 'ejemplo.dlib' --SEGMENT 'PRUEBA2' --BLOCK 'class_prueba'")
code = prompt.cin("READ 'ejemplo.dla' --SEGMENT 'PRUEBA2' --BLOCK 'class_prueba'")

LibsCompiler.Compile.run(code)
LibsCompiler.DLA.delete_cache()

#LibsCompiler.DLA.deconstruct("saved.dla")
