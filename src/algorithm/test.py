'''
Created on Jan 17, 2017

@author: Melvin Laux
'''
import unittest
import numpy as np
from src.algorithm.forward_backward import forward_pass, backward_pass
from src.algorithm import bac
from numpy import allclose
from src.expectations import expec_joint_t, expec_t
from src.baselines.ibcc import calc_q_A, calc_q_pi, expec_t, expec_t_trans


class Test(unittest.TestCase):

    def test_forward_pass(self):
        initProbs = np.array([.5,.5])
        lnA = np.array([[.7,.3],[.3,.7]])
        lnPi = np.array([[.9,.1],[.2,.8]])
        C = np.array([0,0,1,0,0])
        
        doc_start = np.array([1,0,0,0,0])
        
        alphas = forward_pass(C, lnA, lnPi, initProbs, doc_start)
        
        target = np.array([[.8182,.1818],[.8834,.1166],[.1907,.8093],[.7308,.2692],[.8673,.1327]])
        
        assert allclose(alphas,target,atol=1e-4)
        
  #  def test_backward_pass(self):
  #      A = np.array([[.7,.3],[.3,.7]])
  #      C = np.array([[.9,.1],[.2,.8]])
  #      y = np.array([0,0,1,0,0])
  #      
  #      betas = backward_pass(y, A, C)
        
  #      target = np.array([[.6469,.3531],[.5923,.4077],[.3763,.6237],[.6533,.3467],[.6273,.3727],[1,1]])
        
  #      assert allclose(betas,target,atol=1e-4)
        
    def test_bac(self):
        C = np.ones((10,6)) * 1
        
        print C
        
        doc_start = np.zeros((10,1))
        doc_start[[0,2]] = 1
        
        myBac = bac.BAC(L=3, T=10, K=6)
        
        print myBac.run(C, doc_start)


if __name__ == "__main__":
    unittest.main()