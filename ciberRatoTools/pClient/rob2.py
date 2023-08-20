
#ultima versao

import math
import sys
from croblink import *
from math import *
import xml.etree.ElementTree as ET

CELLROWS=7
CELLCOLS=14

class MyRob(CRobLinkAngs):
    def __init__(self, rob_name, rob_id, angles, host):
        CRobLinkAngs.__init__(self, rob_name, rob_id, angles, host)
        self.flag = 'nada'
        self.matriz = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
        self.x_inicial = 0
        self.y_inicial = 0

        self.x_atual = 0
        self.y_atual = 0

        self.count = 0
        self.boost = 0

        self.intersecao = 'false'
        self.cond_inicial = 'true'

        self.char_anterior = ' '
        self.char_atual = ' '
        self.contador = 0

        self.orientacao_anterior = ''
        self.orientacao_atual = ''

        self.guarda_bits_nas_curvas = []
        
        self.intersecao_T = 'false'
        self.intersecao_MAIS = 'false'

        self.bussola_antes = 0

        self.dic = {}
    # In this map the center of cell (i,j), (i in 0..6, j in 0..13) is mapped to labMap[i*2][j*2].
    # to know if there is a wall on top of cell(i,j) (i in 0..5), check if the value of labMap[i*2+1][j*2] is space or not
    def setMap(self, labMap):
        self.labMap = labMap

    def printMap(self):
        for l in reversed(self.labMap):
            print(''.join([str(l) for l in l]))

    def ver_direita(self):
        print(self.x_atual )
        print(self.y_atual )
        print(self.matriz[ self.x_atual ][self.y_atual])
        
        if(self.matriz[ self.x_atual ][self.y_atual]) == 'T':
            if(self.orientacao_atual=='norte'):
                if self.matriz[ self.x_atual +1][self.y_atual] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if self.matriz[ self.x_atual -1 ][self.y_atual ] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if self.matriz[ self.x_atual][self.y_atual+1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if self.matriz[ self.x_atual ][ self.y_atual-1] != ' ':
                    return 'true'
            return 'false'
        else:
            if(self.orientacao_atual=='norte'):
                if self.matriz[ self.x_atual +1][self.y_atual +1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if self.matriz[ self.x_atual -1 ][self.y_atual -1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if self.matriz[ self.x_atual-1][self.y_atual+1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if self.matriz[ self.x_atual +1][ self.y_atual-1] != ' ':
                    return 'true'
            return 'false'

    def ver_esquerda(self):
        print(self.x_atual )
        print(self.y_atual )
        print(self.matriz[ self.x_atual ][self.y_atual])
        if(self.matriz[ self.x_atual ][self.y_atual]) == 'T':    
            if(self.orientacao_atual=='norte'):
                if self.matriz[ self.x_atual -1 ][ self.y_atual ] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if self.matriz[ self.x_atual +1][ self.y_atual] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if self.matriz[ self.x_atual][ self.y_atual-1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if self.matriz[ self.x_atual][ self.y_atual +1] != ' ':
                    return 'true'
            return 'false'
        else:   
            if(self.orientacao_atual=='norte'):
                if self.matriz[ self.x_atual -1 ][ self.y_atual +1 ] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if self.matriz[ self.x_atual +1][ self.y_atual-1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if self.matriz[ self.x_atual-1][ self.y_atual-1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if self.matriz[ self.x_atual+1][ self.y_atual +1] != ' ':
                    return 'true'
            return 'false'

    
    def ver_frente(self):
        if(self.orientacao_atual=='norte'):
            if self.matriz[ self.x_atual ][ self.y_atual] +1 != ' ':
                return 'true'
        elif(self.orientacao_atual=='sul'):
            if self.matriz[ self.x_atual  ][self.y_atual -1] != ' ':
                return 'true'
        elif(self.orientacao_atual=='oeste'):
            if self.matriz[ self.x_atual +1][ self.y_atual] != ' ':
                return 'true'
        elif(self.orientacao_atual=='este'):
            if self.matriz[ self.x_atual -1 ][ self.y_atual] != ' ':
                return 'true'
        return 'false'

    def next_T(self):
        
        print('atual')

        

        if self.matriz[self.x_atual][self.y_atual] == 'T':
            print('atual')
            print(self.matriz[self.x_atual][self.y_atual])
            return 'true'
        
        elif(self.orientacao_atual=='norte'):
            if self.matriz[ self.x_atual ][ self.y_atual + 1] == 'T':
                print('next')
                print(self.matriz[ self.x_atual ][ self.y_atual + 1])
                return 'true'
        elif(self.orientacao_atual=='sul'):
            if self.matriz[ self.x_atual  ][self.y_atual -1] == 'T':
                print('next')
                print(self.matriz[ self.x_atual  ][self.y_atual -1])
                return 'true'
        elif(self.orientacao_atual=='oeste'):
            if self.matriz[ self.x_atual -1][ self.y_atual] == 'T':
                print('next')
                print(self.matriz[ self.x_atual -1][ self.y_atual])
                return 'true'
        elif(self.orientacao_atual=='este'):
            if self.matriz[ self.x_atual +1 ][ self.y_atual] == 'T':
                print('next')
                print(self.matriz[ self.x_atual +1 ][ self.y_atual])
                return 'true'
        return 'false'



    def run(self):
        if self.status != 0:
            print("Connection refused or error")
            quit()

        state = 'stop'
        stopped_state = 'run'

        while True:
            self.readSensors()

            if self.measures.endLed:
                print(self.rob_name + " exiting")
                quit()

            if state == 'stop' and self.measures.start:
                state = stopped_state

            if state != 'stop' and self.measures.stop:
                stopped_state = state
                state = 'stop'

            if state == 'run':
                if self.measures.visitingLed==True:
                    state='wait'
                if self.measures.ground==0:
                    self.setVisitingLed(True);
                self.wander()
            elif state=='wait':
                self.setReturningLed(True)
                if self.measures.visitingLed==True:
                    self.setVisitingLed(False)
                if self.measures.returningLed==True:
                    state='return'
                self.driveMotors(0.0,0.0)
            elif state=='return':
                if self.measures.visitingLed==True:
                    self.setVisitingLed(False)
                if self.measures.returningLed==True:
                    self.setReturningLed(False)
                self.wander()
            

            
   

    def wander(self):
        center_id = 0
        left_id = 1
        right_id = 2
        back_id = 3
        print(self.measures.lineSensor)
        # print('Bussola')
        # print(self.measures.compass)
        
       
        # print('GPS')
        # print(self.measures.x)
        # print(self.measures.y)

        print(self.orientacao_atual)
        if self.measures.compass <= 105 and self.measures.compass > 75 :
            self.orientacao_atual = 'oeste'
        elif self.measures.compass > -105 and self.measures.compass <= -75:
            self.orientacao_atual = 'este'
        elif self.measures.compass <= 15 and self.measures.compass > -15  :
            self.orientacao_atual = 'norte'
        elif  self.measures.compass > 165 or self.measures.compass <= -165:
            self.orientacao_atual = 'sul'      

        if self.cond_inicial=='true':
            self.x_inicial = self.measures.y
            self.x_atual = self.measures.y
            self.y_inicial = self.measures.x
            self.y_atual = self.measures.x

            self.x_atual = -self.x_atual + self.x_inicial + 11 
            self.y_atual = self.y_atual - self.y_inicial + 25 
            self.x_atual = round(self.x_atual)
            self.y_atual = round(self.y_atual)


           
           
            self.matriz[self.x_atual][self.y_atual] = 'I'
            self.char_atual = 'I'
            self.cond_inicial='false'
            self.bussola_antes = self.measures.compass


            
            
        else:
            self.x_atual = self.measures.y
            self.y_atual = self.measures.x

            self.x_atual = -self.x_atual + self.x_inicial + 11 
            self.y_atual = self.y_atual - self.y_inicial + 25 

          

            self.x_atual = round(self.x_atual)
            self.y_atual =round(self.y_atual)
        

        
     
        for i in range(len(self.matriz)):
            print(self.matriz[i])
        
        
        
        if self.measures.lineSensor == ['0', '0', '0', '0', '0', '0', '0']:
            
            if self.flag == 'nada_esquerda':
               
                self.driveMotors(0.0,-0.15)
                
                self.flag = 'nada'
            elif self.flag == 'nada_direita':
                
                self.driveMotors(-0.15,0.0)
                
                self.flag = 'nada'
            else:
                
                self.driveMotors(-0.01,-0.01)
            
        elif self.measures.lineSensor == ['1', '0', '0', '0', '0', '0', '0']:
            self.driveMotors(-0.03,0.00)
        # elif self.measures.lineSensor == ['0', '1', '0', '0', '0', '0', '0']:
        #     self.driveMotors(-0.02,0.00)
        # elif self.measures.lineSensor == ['0', '0', '0', '0', '0', '1', '0']:
        #     self.driveMotors(0.00,-0.02)    
        elif self.measures.lineSensor == ['0', '0', '0', '0', '0', '0', '1']:
            self.driveMotors(0.00,-0.03)
            

        if self.intersecao_T == 'true':

            self.flag = 'left'

        if self.flag == 'frente_intersecao' :
            
            if self.boost < 2:

                if self.count < 5:
                    self.driveMotors(0.10,0.10)
                    self.count = self.count + 1 
                else:
                    self.flag = 'nada'
                    self.count = 0
                    self.boost = 0
            else:
                self.flag = 'nada'
                self.matriz[self.x_atual][self.y_atual] = 'o'
                self.boost = 0


            # else:
            #     if(self.ver_esquerda()=='false'):
            #         self.flag = 'left'
            #     elif (self.ver_direita()=='false'):
            #         self.flag = 'left'
            #     else:
            #         self.flag = 'nada'
            #     self.boost = 0



        elif self.flag == 'left' :
            
            
           
            self.driveMotors(-0.02,0.08)
            
            self.guarda_bits_nas_curvas.append(self.measures.lineSensor)
                
            if(self.orientacao_atual != self.orientacao_anterior):   
                self.flag = 'nada_esquerda'
                matriz_x = self.x_atual
                matriz_y = self.y_atual

                if self.intersecao_T == 'true':
                    for x in self.guarda_bits_nas_curvas[3:]:
                      
                        if x[4:] == ['1','1','1']:
                            self.intersecao_MAIS = 'true'
                            self.intersecao_T = 'false'
                            
                        

                else:
                    for x in self.guarda_bits_nas_curvas:
                      
                        if x[4:] == ['1','1','1']:
                            self.intersecao = 'true'

                

                if (self.matriz[matriz_x][matriz_y] == ' ' or self.matriz[matriz_x][matriz_y] == 'o') and (self.intersecao == 'true' or self.intersecao_T == 'true'):
                    self.matriz[matriz_x][matriz_y] = 'T'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                elif self.matriz[matriz_x][matriz_y] == ' ' and self.intersecao_MAIS == 'true':
                    self.matriz[matriz_x][matriz_y] = '+'
                    #print(self.intersecao_MAIS)
                    self.intersecao_MAIS = 'false'
                elif self.matriz[matriz_x][matriz_y] == ' ' and self.intersecao != 'true':
                    self.matriz[matriz_x][matriz_y] = 'o'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                self.guarda_bits_nas_curvas = []
                # if self.measures.lineSensor == ['0', '0', '1', '1', '1', '0', '0'] or self.measures.lineSensor == ['0', '1', '1', '1', '0', '0', '0'] or self.measures.lineSensor == ['0', '0', '0', '1', '1', '0', '0'] or self.measures.lineSensor == ['0', '0', '0', '1', '1', '1', '0'] or  self.measures.lineSensor == ['0', '0', '1', '1', '0', '0', '0'] :
                #     self.flag = 'nada'
        elif self.flag == 'right' :
        
            self.driveMotors(0.08,-0.02)
            
            self.guarda_bits_nas_curvas.append(self.measures.lineSensor)
            if(self.orientacao_atual != self.orientacao_anterior):
                self.flag = 'nada_direita'
                matriz_x = self.x_atual
                matriz_y = self.y_atual

                if self.intersecao_T == 'true':
                    for x in self.guarda_bits_nas_curvas[:3]:
                        print(x)
                        if x[:3] == ['1','1','1']:
                            self.intersecao_MAIS = 'true'
                            self.intersecao_T = 'false'
                           
                        
                        

                else:
                    for x in self.guarda_bits_nas_curvas:
                        print(x)
                        if x[:3] == ['1','1','1']:
                            self.intersecao = 'true'
                           





                # for x in self.guarda_bits_nas_curvas:
                    
                #     if x[:3] == ['1','1','1']:
                #         self.intersecao = 'true'
                # print(self.intersecao)

                
                if (self.matriz[matriz_x][matriz_y] == ' ' or self.matriz[matriz_x][matriz_y] == 'o') and (self.intersecao == 'true' or self.intersecao_T == 'true'):
                    self.matriz[matriz_x][matriz_y] = 'T'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                    

                elif self.matriz[matriz_x][matriz_y] == ' ' and self.intersecao_MAIS == 'true':
                    self.matriz[matriz_x][matriz_y] = '+'
                    
                    self.intersecao_MAIS = 'false'   
                elif self.matriz[matriz_x][matriz_y] == ' ' and self.intersecao != 'true':
                    self.matriz[matriz_x][matriz_y] = 'o'
                    self.intersecao = 'false'
                self.guarda_bits_nas_curvas = []
                # if self.measures.lineSensor == ['0', '0', '1', '1', '1', '0', '0'] or self.measures.lineSensor == ['0', '1', '1', '1', '0', '0', '0'] or self.measures.lineSensor == ['0', '0', '0', '1', '1', '0', '0'] or self.measures.lineSensor == ['0', '0', '0', '1', '1', '1', '0'] or  self.measures.lineSensor == ['0', '0', '1', '1', '0', '0', '0'] :
                #     self.flag = 'nada'
            
        else:
            if self.measures.lineSensor == ['0', '1', '1', '1', '0', '0', '0'] :
                self.driveMotors(0.04,0.09)
                self.flag = 'frente'
                
            elif self.measures.lineSensor == ['0', '1', '1', '0', '0', '0', '0']:
                self.driveMotors(0.07,0.09)
                self.flag = 'frente'
                
            elif self.measures.lineSensor == ['0', '0', '1', '1', '1', '0', '0']:
                self.driveMotors(0.09,0.09)
                self.flag = 'frente'  
            elif self.measures.lineSensor == ['0', '0', '0', '1', '1', '0', '0'] :
                self.driveMotors(0.09,0.08)
                self.flag = 'frente'
                
            elif self.measures.lineSensor == ['0', '0', '0', '1', '1', '1', '0'] :
                self.driveMotors(0.09,0.04)
                self.flag = 'frente'
                
            elif self.measures.lineSensor == ['0', '0', '0', '0', '1', '1', '0'] :
                self.driveMotors(0.09,0.07)
                self.flag = 'frente'
                
            elif self.measures.lineSensor == ['0', '1', '1', '1', '1', '1', '0'] :
                self.driveMotors(0.04,0.04)
                self.flag = 'frente'
                
            elif self.measures.lineSensor == ['0', '0', '1', '1', '0', '0', '0'] :
                self.driveMotors(0.08,0.09)
                self.flag = 'frente'
            
           
                
            elif self.measures.lineSensor == ['0', '0', '0', '1', '1', '1', '1']:
               
                
                if (self.ver_direita() == 'true' and self.next_T() == 'true'):
                    print()
                    self.flag = 'frente_intersecao'
                    self.boost = self.boost + 1
                    print('DEVIA IR EM FRENTEEEEEEEE')
                else:
                    self.flag = 'right'
                
        
            
            elif self.measures.lineSensor == ['0', '0', '1', '1', '1', '1', '1']:
                print('right')
                print('OLAAAAAAAAAAAAAAAAAAA')
                print(self.ver_direita())
                # if self.matriz[self.x_atual][self.y_atual] == 'T':
                if (self.ver_direita() == 'true' and self.next_T() == 'true' ):
                    print('DEVIA IR EM FRENTEEEEEEEE')
                    self.flag = 'frente_intersecao'
                    self.boost = self.boost + 1
                else:
                    self.flag = 'right'
                # else:
                # # elif  self.matriz[self.x_atual][self.y_atual] == ' ' or self.matriz[self.x_atual][self.y_atual] == 'o' :
                #     self.flag = 'right'
                self.contador = 0
            
            elif self.measures.lineSensor == ['1', '1', '1', '1', '0', '0', '0']:
               
                #if self.matriz[self.x_atual][self.y_atual] == 'T':
                if (self.ver_esquerda() == 'true' and self.next_T() == 'true'):
                    print('DEVIA IR EM FRENTEEEEEEEE')
                    self.flag = 'frente_intersecao'
                    self.boost = self.boost + 1
                else:
                    self.flag = 'left'
                #else:
                # elif  self.matriz[self.x_atual][self.y_atual] == ' ' or self.matriz[self.x_atual][self.y_atual] == 'o' :
                    # self.flag = 'left'
                
    
            elif self.measures.lineSensor == ['1', '1', '1', '1', '1', '0', '0']:
              
                self.contador = 0
               
                
                # if self.matriz[self.x_atual][self.y_atual] == 'T':
                    
                if (self.ver_esquerda() == 'true' and self.next_T() == 'true'):
                    print('DEVIA IR EM FRENTEEEEEEEE')
                    self.flag = 'frente_intersecao'
                    self.boost = self.boost + 1
                else:
                    self.flag = 'left'
                        
                # else:
                # # elif  self.matriz[self.x_atual][self.y_atual] == ' ' or self.matriz[self.x_atual][self.y_atual] == 'o' :
                #     self.flag = 'left'
            
            elif self.measures.lineSensor == ['1', '1', '1', '1', '1', '1', '1']:
                self.intersecao_T = 'true'
                # self.flag = 'left'
            
        
       
        matriz_x = self.x_atual
        matriz_y = self.y_atual

        diferenca = abs(abs(self.bussola_antes) - abs(self.measures.compass))
        

      

        
        if self.matriz[matriz_x][matriz_y] == ' ':
            if self.measures.compass < 100 and self.measures.compass > 80 or self.measures.compass > -100 and self.measures.compass < -80:
                if self.flag != 'right' and self.flag != 'left'  :
                    self.matriz[matriz_x][matriz_y] = '|'   
                    self.char_antes = '|'
                    
            elif self.measures.compass < 10 and self.measures.compass > -10  or  self.measures.compass > 170  or self.measures.compass < -170:
                if self.flag != 'right' and self.flag != 'left' :
                    self.matriz[matriz_x][matriz_y] = '-'
                    self.char_antes = '-'
                    
            # elif self.intersecao == 'true'  or diferenca > 25 :
            #     self.intersecao = 'false'
            #     self.matriz[matriz_x][matriz_y] = '+'
            #     self.char_antes = '+'
            #     print('inter ',diferenca)

       
    
               



        # print(self.char_anterior)
        self.char_anterior = self.char_atual
        
        self.bussola_antes = self.measures.compass

        self.orientacao_anterior = self.orientacao_atual
        
        

    

        

class Map():
    def __init__(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        
        self.labMap = [[' '] * (CELLCOLS*2-1) for i in range(CELLROWS*2-1) ]
        i=1
        for child in root.iter('Row'):
           line=child.attrib['Pattern']
           row =int(child.attrib['Pos'])
           if row % 2 == 0:  # this line defines vertical lines
               for c in range(len(line)):
                   if (c+1) % 3 == 0:
                       if line[c] == '|':
                           self.labMap[row][(c+1)//3*2-1]='|'
                       else:
                           None
           else:  # this line defines horizontal lines
               for c in range(len(line)):
                   if c % 3 == 0:
                       if line[c] == '-':
                           self.labMap[row][c//3*2]='-'
                       else:
                           None
               
           i=i+1


rob_name = "pClient1"
host = "localhost"
pos = 1
mapc = None

for i in range(1, len(sys.argv),2):
    if (sys.argv[i] == "--host" or sys.argv[i] == "-h") and i != len(sys.argv) - 1:
        host = sys.argv[i + 1]
    elif (sys.argv[i] == "--pos" or sys.argv[i] == "-p") and i != len(sys.argv) - 1:
        pos = int(sys.argv[i + 1])
    elif (sys.argv[i] == "--robname" or sys.argv[i] == "-r") and i != len(sys.argv) - 1:
        rob_name = sys.argv[i + 1]
    elif (sys.argv[i] == "--map" or sys.argv[i] == "-m") and i != len(sys.argv) - 1:
        mapc = Map(sys.argv[i + 1])
    else:
        print("Unkown argument", sys.argv[i])
        quit()

if __name__ == '__main__':
    rob=MyRob(rob_name,pos,[0.0,60.0,-60.0,180.0],host)
    if mapc != None:
        rob.setMap(mapc.labMap)
        rob.printMap()
    
    rob.run()
