# -*- coding: utf-8 -*-
"""
Módulo de Materiais

@author: César Eduardo Petersen

@date: Mon Sep  6 17:33:10 2021

Inclui Definição de Materiais e Leis constitutivas.

"""

import numpy as np

class Material:
    def __init__(self, E, nu, t):
        """
        Define um material elastico-linear homogêneo.

        Args:
            E (float): Módulo de Elasticidade.
            nu (float): Coeficiente de Poisson.
            t (float): Espessura, caso esteja no Estado Plano de Tensões, ou
                       nulo para considerar Estado Plano de Deformações

        Returns:
            None.

        """
        self.E = E
        self.nu = nu
        
        # propriedades derivadas
        self.G = E/(2*(1+nu))
        self.K = E/(3*(1-2*nu))
        self.lame = self.K-2*self.G/3
        
        self.t = t
        self.EPT = (t > 0)
        
    def De(self, **kwargs):
        """
        Define uma matriz constitutiva para elementos bidimensionais

        Args:
            **kwargs (dict): dicionario de parametros extras para o modelo, opcional.

        Returns:
            float[3][3]: Matriz constitutiva do elemento.

        """
        E = self.E
        nu = self.nu
        if(self.EPT):
            return (E/(1-nu*nu))*np.array(
                [[ 1,nu, 0],
                 [nu, 1, 0],
                 [ 0, 0, (1-nu)/2]]
                , dtype='float32')
        else:
            return (E/((1-nu)*(1-2*nu)))*np.array(
                [[1-nu,  nu, 0],
                 [ nu ,1-nu, 0],
                 [  0 ,  0 , (1-2*nu)/2]]
                , dtype='float32')
