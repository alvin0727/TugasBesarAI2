#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt


# In[19]:

def hitungGerd(gejala1,gejala2,gejala3,gejala4,gejala5,gejala6,gejala7):
    # Input nilai untuk setiap gejala
    g1_heartburn_input = gejala1
    g2_mual_input = gejala2
    g3_regurgitation_input = gejala3
    g4_sulit_menelan_input = gejala4
    g5_darah_input = gejala5
    g6_sakit_dada_input = gejala6
    g7_batuk_input = gejala7


    # In[20]:


    # Definisikan range nilai untuk gejala dari 0-100 dalam array
    g1_heartburn = np.arange(0, 11)
    g2_mual = np.arange(0, 11)
    g3_regurgitation = np.arange(0,11)
    g4_sulit_menelan = np.arange(0,11)
    g5_darah = np.arange(0,11)
    g6_sakit_dada = np.arange(0,11)
    g7_batuk = np.arange(0,11)

    gerd_range = np.arange(0,11)


    # In[21]:


    # Mendefinisikan himpunan fuzzy untuk setiap gejala

    # Heartburn -> Rasa terbakar di dada dan kerongkongan
    g1_heartburn_mild = mf.trapmf(g1_heartburn, [0, 0, 1, 4])
    g1_heartburn_moderate = mf.trapmf(g1_heartburn, [2, 5, 5, 8])
    g1_heartburn_severe = mf.trapmf(g1_heartburn, [6, 9, 10, 12])

    # In[22]:


    # Mual
    g2_mual_mild = mf.trapmf(g2_mual, [0, 0, 1, 4])
    g2_mual_moderate = mf.trapmf(g2_mual, [2, 5, 5, 8])
    g2_mual_severe = mf.trapmf(g2_mual, [6, 9, 10, 12])


    # In[23]:


    # Regurgitation -> Isi perut naik lagi ke kerongkongan
    g3_regurgitation_mild = mf.trapmf(g3_regurgitation, [0, 0, 1, 4])
    g3_regurgitation_moderate = mf.trapmf(g3_regurgitation, [2, 5, 5, 8])
    g3_regurgitation_severe = mf.trapmf(g3_regurgitation, [6, 9, 10, 12])


    # In[24]:


    # Sulit menelan
    g4_sulit_menelan_mild = mf.trapmf(g4_sulit_menelan, [0, 0, 1, 4])
    g4_sulit_menelan_moderate = mf.trapmf(g4_sulit_menelan, [2, 5, 5, 8])
    g4_sulit_menelan_severe = mf.trapmf(g4_sulit_menelan, [6, 9, 10, 12])



    # In[25]:


    # Darah -> Ada darah di air liur, muntah, atau pada kotoran
    g5_darah_mild = mf.trapmf(g5_darah, [0, 0, 1, 4])
    g5_darah_moderate = mf.trapmf(g5_darah, [2, 5, 5, 8])
    g5_darah_severe = mf.trapmf(g5_darah, [6, 9, 10, 12])

    # In[26]:


    # Sakit dada
    g6_sakit_dada_mild = mf.trapmf(g6_sakit_dada, [0, 0, 1, 4])
    g6_sakit_dada_moderate = mf.trapmf(g6_sakit_dada, [2, 5, 5, 8])
    g6_sakit_dada_severe = mf.trapmf(g6_sakit_dada, [6, 9, 10, 12])

    # In[27]:


    # Batuk
    g7_batuk_mild = mf.trapmf(g7_batuk, [0, 0, 1, 4])
    g7_batuk_moderate = mf.trapmf(g7_batuk, [2, 5, 5, 8])
    g7_batuk_severe = mf.trapmf(g7_batuk, [6, 9, 10, 12])


    # In[28]:


    # Definisikan range untuk penyakit GERD
    gerd_very_mild = mf.trapmf(gerd_range, [-2, 0, 1, 3])
    gerd_mild = mf.trapmf(gerd_range, [1, 3, 3, 5])
    gerd_moderate = mf.trapmf(gerd_range, [3, 5, 5, 7])
    gerd_severe = mf.trapmf(gerd_range, [5, 7, 7, 9])
    gerd_very_severe = mf.trapmf(gerd_range, [7, 9, 12, 15])


    # In[29]:


    # Interpolasi keanggotaan fuzzy
    # Mencari tahu nilai keanggotaan dari input gejala oleh user

    g1_heartburn_mild_val = fuzz.interp_membership(g1_heartburn, g1_heartburn_mild, g1_heartburn_input)
    g1_heartburn_moderate_val = fuzz.interp_membership(g1_heartburn, g1_heartburn_moderate, g1_heartburn_input)
    g1_heartburn_severe_val = fuzz.interp_membership(g1_heartburn, g1_heartburn_severe, g1_heartburn_input)

    g2_mual_mild_val = fuzz.interp_membership(g2_mual, g2_mual_mild, g2_mual_input)
    g2_mual_moderate_val = fuzz.interp_membership(g2_mual, g2_mual_moderate, g2_mual_input)
    g2_mual_severe_val = fuzz.interp_membership(g2_mual, g2_mual_severe, g2_mual_input)

    g3_regurgitation_mild_val = fuzz.interp_membership(g3_regurgitation, g3_regurgitation_mild, g3_regurgitation_input)
    g3_regurgitation_moderate_val = fuzz.interp_membership(g3_regurgitation, g3_regurgitation_moderate, g3_regurgitation_input)
    g3_regurgitation_severe_val = fuzz.interp_membership(g3_regurgitation, g3_regurgitation_severe, g3_regurgitation_input)

    g4_sulit_menelan_mild_val = fuzz.interp_membership(g4_sulit_menelan, g4_sulit_menelan_mild, g4_sulit_menelan_input)
    g4_sulit_menelan_moderate_val = fuzz.interp_membership(g4_sulit_menelan, g4_sulit_menelan_moderate, g4_sulit_menelan_input)
    g4_sulit_menelan_severe_val = fuzz.interp_membership(g4_sulit_menelan, g4_sulit_menelan_severe, g4_sulit_menelan_input)

    g5_darah_mild_val = fuzz.interp_membership(g5_darah, g5_darah_mild, g5_darah_input)
    g5_darah_moderate_val = fuzz.interp_membership(g5_darah, g5_darah_moderate, g5_darah_input)
    g5_darah_severe_val = fuzz.interp_membership(g5_darah, g5_darah_severe, g5_darah_input)

    g6_sakit_dada_mild_val = fuzz.interp_membership(g6_sakit_dada, g6_sakit_dada_mild, g6_sakit_dada_input)
    g6_sakit_dada_moderate_val = fuzz.interp_membership(g6_sakit_dada, g6_sakit_dada_moderate, g6_sakit_dada_input)
    g6_sakit_dada_severe_val = fuzz.interp_membership(g6_sakit_dada, g6_sakit_dada_severe, g6_sakit_dada_input)

    g7_batuk_mild_val = fuzz.interp_membership(g7_batuk, g7_batuk_mild, g7_batuk_input)
    g7_batuk_moderate_val = fuzz.interp_membership(g7_batuk, g7_batuk_moderate, g7_batuk_input)
    g7_batuk_severe_val = fuzz.interp_membership(g7_batuk, g7_batuk_severe, g7_batuk_input)

    # Ruleset untuk fuzzy
    # Ada 70 rules yang kami gunakan

    # Very Severe
    rule1 = np.fmin(np.fmin(g1_heartburn_severe_val,g3_regurgitation_severe_val), gerd_very_severe)
    rule2 = np.fmin(np.fmin(g1_heartburn_severe_val,g6_sakit_dada_severe_val), gerd_very_severe)
    rule3 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_severe_val), g4_sulit_menelan_severe_val), g5_darah_moderate_val), g7_batuk_severe_val), gerd_very_severe)
    rule4 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_severe_val), g3_regurgitation_moderate_val), g5_darah_severe_val), gerd_very_severe)
    rule5 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val ,g4_sulit_menelan_moderate_val), g5_darah_severe_val), g7_batuk_severe_val), gerd_very_severe)
    rule6 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val ,g4_sulit_menelan_severe_val), g6_sakit_dada_moderate_val), g7_batuk_moderate_val), gerd_very_severe)
    rule7 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g2_mual_severe_val), g3_regurgitation_mild_val), g4_sulit_menelan_severe_val), g5_darah_severe_val),g6_sakit_dada_moderate_val),g7_batuk_severe_val), gerd_very_severe)
    rule8 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_moderate_val), g4_sulit_menelan_moderate_val), g5_darah_moderate_val), g6_sakit_dada_moderate_val),g7_batuk_moderate_val), gerd_very_severe)
    rule9 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val, g3_regurgitation_severe_val), g5_darah_severe_val), g6_sakit_dada_severe_val), gerd_very_severe)
    rule10 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val, g3_regurgitation_severe_val), g5_darah_severe_val), g6_sakit_dada_moderate_val), gerd_very_severe)
    rule11 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val, g3_regurgitation_severe_val), g5_darah_moderate_val), g6_sakit_dada_severe_val), gerd_very_severe)
    rule12 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val, g3_regurgitation_moderate_val), g5_darah_severe_val), g6_sakit_dada_severe_val), gerd_very_severe)
    rule13 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g3_regurgitation_severe_val), g5_darah_severe_val), g6_sakit_dada_severe_val), gerd_very_severe)
    rule14 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val, g3_regurgitation_severe_val), g5_darah_severe_val), g6_sakit_dada_severe_val), gerd_very_severe)
    rule15 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val, g3_regurgitation_mild_val), g5_darah_severe_val), g6_sakit_dada_severe_val), gerd_very_severe)
    
    # Severe
    rule16 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val ,g3_regurgitation_moderate_val), g4_sulit_menelan_severe_val), g5_darah_mild_val), g7_batuk_moderate_val), gerd_severe)
    rule17 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g3_regurgitation_severe_val), g4_sulit_menelan_mild_val), g5_darah_moderate_val), g6_sakit_dada_mild_val), gerd_severe)
    rule18 = np.fmin(np.fmin(g1_heartburn_moderate_val ,g3_regurgitation_moderate_val), gerd_severe)
    rule19 = np.fmin(np.fmin(g3_regurgitation_severe_val ,g4_sulit_menelan_severe_val), gerd_severe)
    rule20 = np.fmin(np.fmin(np.fmin(np.fmin(g2_mual_moderate_val,g3_regurgitation_moderate_val), g4_sulit_menelan_moderate_val), g7_batuk_moderate_val), gerd_severe)
    rule21 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g2_mual_mild_val), g4_sulit_menelan_severe_val), g5_darah_mild_val), g6_sakit_dada_mild_val), gerd_severe)
    rule22 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g2_mual_moderate_val), g4_sulit_menelan_mild_val), g6_sakit_dada_severe_val), g7_batuk_severe_val), gerd_severe)
    rule23 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val,g3_regurgitation_moderate_val), g5_darah_mild_val), g6_sakit_dada_mild_val), gerd_severe)
    rule24 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val ,g2_mual_moderate_val), g3_regurgitation_severe_val), g4_sulit_menelan_moderate_val), g5_darah_moderate_val),g6_sakit_dada_moderate_val),g7_batuk_moderate_val), gerd_severe)
    rule25 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g3_regurgitation_severe_val), g4_sulit_menelan_moderate_val), g6_sakit_dada_moderate_val), g7_batuk_severe_val), gerd_severe)
    rule26 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val ,g2_mual_severe_val), g4_sulit_menelan_moderate_val), g5_darah_moderate_val), g7_batuk_moderate_val), gerd_severe)
    rule27 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val ,g2_mual_moderate_val), g4_sulit_menelan_severe_val), g5_darah_moderate_val), g7_batuk_severe_val), gerd_severe)
    rule28 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g3_regurgitation_moderate_val), g4_sulit_menelan_severe_val), g7_batuk_severe_val), gerd_severe)
    rule29 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g3_regurgitation_moderate_val), g4_sulit_menelan_severe_val), g6_sakit_dada_moderate_val), gerd_severe)
    rule30 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_severe_val ,g2_mual_moderate_val), g4_sulit_menelan_moderate_val), g5_darah_severe_val), g6_sakit_dada_moderate_val), gerd_severe)

    # Moderate
    rule31 = np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val,g3_regurgitation_mild_val), g4_sulit_menelan_moderate_val), gerd_moderate)
    rule32 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val,g2_mual_mild_val), g4_sulit_menelan_severe_val), g7_batuk_mild_val), gerd_moderate)
    rule33 = np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val,g3_regurgitation_mild_val), g5_darah_mild_val), gerd_moderate)
    rule34 = np.fmin(np.fmin(np.fmin(np.fmin(g2_mual_severe_val,g3_regurgitation_moderate_val), g4_sulit_menelan_moderate_val), g7_batuk_mild_val), gerd_moderate)
    rule35 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val,g2_mual_moderate_val), g4_sulit_menelan_mild_val), g7_batuk_mild_val), gerd_moderate)
    rule36 = np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val,g3_regurgitation_mild_val), g5_darah_moderate_val), g7_batuk_moderate_val), gerd_moderate)
    rule37 = np.fmin(np.fmin(np.fmin(g2_mual_severe_val,g3_regurgitation_moderate_val), g4_sulit_menelan_moderate_val), gerd_moderate)
    rule38 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_mild_val), g3_regurgitation_moderate_val), g4_sulit_menelan_mild_val), g5_darah_moderate_val),g6_sakit_dada_moderate_val),g7_batuk_mild_val), gerd_moderate)
    rule39 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g2_mual_mild_val), g3_regurgitation_mild_val), g4_sulit_menelan_severe_val), g5_darah_mild_val),g6_sakit_dada_moderate_val),g7_batuk_mild_val), gerd_moderate)
    rule40 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_mild_val), g3_regurgitation_mild_val), g4_sulit_menelan_mild_val), g5_darah_mild_val),g6_sakit_dada_moderate_val),g7_batuk_mild_val), gerd_moderate)
    rule41 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_moderate_val), g3_regurgitation_moderate_val), g4_sulit_menelan_moderate_val), g5_darah_mild_val),g6_sakit_dada_moderate_val),g7_batuk_mild_val), gerd_moderate)
    rule42 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_mild_val), g3_regurgitation_moderate_val), g4_sulit_menelan_mild_val), g5_darah_mild_val),g6_sakit_dada_moderate_val),g7_batuk_mild_val), gerd_moderate)
    rule43 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_mild_val), g3_regurgitation_moderate_val), g4_sulit_menelan_mild_val), g5_darah_mild_val),g6_sakit_dada_mild_val),g7_batuk_moderate_val), gerd_moderate)
    rule44 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val ,g2_mual_moderate_val), g3_regurgitation_moderate_val), g4_sulit_menelan_mild_val), g5_darah_mild_val),g6_sakit_dada_mild_val),g7_batuk_moderate_val), gerd_moderate)

    # Mild
    rule45 = np.fmin(np.fmin(g1_heartburn_mild_val,g3_regurgitation_mild_val), gerd_mild)
    rule46 = np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val,g4_sulit_menelan_moderate_val),g7_batuk_mild_val), gerd_mild)
    rule47 = np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val,g2_mual_mild_val),g4_sulit_menelan_moderate_val), gerd_mild)
    rule48 = np.fmin(np.fmin(g1_heartburn_mild_val,g6_sakit_dada_mild_val), gerd_mild)
    rule49 = np.fmin(np.fmin(np.fmin(np.fmin(g2_mual_moderate_val,g3_regurgitation_mild_val),g4_sulit_menelan_mild_val),g7_batuk_mild_val), gerd_mild)
    rule50 = np.fmin(np.fmin(np.fmin(np.fmin(g2_mual_mild_val,g4_sulit_menelan_moderate_val),g5_darah_moderate_val),g7_batuk_moderate_val), gerd_mild)
    rule51 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g2_mual_severe_val), g3_regurgitation_mild_val), g4_sulit_menelan_mild_val), g5_darah_mild_val),g6_sakit_dada_mild_val),g7_batuk_mild_val), gerd_mild)
    rule52 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g2_mual_mild_val), g3_regurgitation_mild_val), g4_sulit_menelan_mild_val), g5_darah_mild_val),g6_sakit_dada_mild_val),g7_batuk_mild_val), gerd_mild)
    rule53 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g2_mual_moderate_val), g3_regurgitation_mild_val), g4_sulit_menelan_moderate_val), g5_darah_mild_val),g6_sakit_dada_mild_val),g7_batuk_moderate_val), gerd_mild)
    rule54 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val ,g2_mual_severe_val), g3_regurgitation_mild_val), g4_sulit_menelan_severe_val), g5_darah_mild_val),g6_sakit_dada_mild_val),g7_batuk_moderate_val), gerd_mild)
    rule55 = np.fmin(np.fmin(np.fmin(g1_heartburn_moderate_val,g2_mual_mild_val),g4_sulit_menelan_mild_val), gerd_mild)
    rule56 = np.fmin(np.fmin(np.fmin(g3_regurgitation_moderate_val,g4_sulit_menelan_mild_val),g7_batuk_mild_val), gerd_mild)
    rule57 = np.fmin(np.fmin(np.fmin(g2_mual_mild_val,g6_sakit_dada_moderate_val),g7_batuk_mild_val), gerd_mild)

    # Very Mild
    rule58 = np.fmin(np.fmin(g1_heartburn_mild_val,g4_sulit_menelan_mild_val), gerd_very_mild)
    rule59 = np.fmin(np.fmin(g2_mual_mild_val,g3_regurgitation_mild_val), gerd_very_mild)
    rule60 = np.fmin(np.fmin(g6_sakit_dada_mild_val,g7_batuk_moderate_val), gerd_very_mild)
    rule61 = np.fmin(np.fmin(np.fmin(g2_mual_mild_val,g4_sulit_menelan_mild_val),g7_batuk_mild_val), gerd_very_mild)
    rule62 = np.fmin(np.fmin(np.fmin(g4_sulit_menelan_mild_val,g5_darah_mild_val),g7_batuk_mild_val), gerd_very_mild)
    rule63 = np.fmin(np.fmin(np.fmin(g1_heartburn_mild_val,g2_mual_mild_val),g4_sulit_menelan_mild_val), gerd_very_mild)
    rule64 = np.fmin(g1_heartburn_mild_val,gerd_very_mild)
    rule65 = np.fmin(np.fmin(g2_mual_mild_val,g3_regurgitation_mild_val), gerd_very_mild)
    rule66 = np.fmin(np.fmin(g1_heartburn_mild_val,g5_darah_mild_val), gerd_very_mild)
    rule67 = np.fmin(np.fmin(g3_regurgitation_mild_val,g6_sakit_dada_mild_val), gerd_very_mild)
    rule68 = np.fmin(np.fmin(np.fmin(g2_mual_mild_val,g4_sulit_menelan_mild_val),g7_batuk_mild_val), gerd_very_mild)
    rule69 = np.fmin(np.fmin(g2_mual_mild_val,g7_batuk_mild_val),gerd_very_mild)
    rule70 = np.fmin(np.fmin(g1_heartburn_mild_val,g4_sulit_menelan_mild_val),gerd_very_mild)


    # In[31]:


    # Proses inference dengan menggunakan metode Mamdani
    gerd_very_severe_result = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax( np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(
        rule1, rule2),rule3),rule4),rule5),rule6),rule7),rule8),rule9),rule10),rule11),rule12),rule13),rule14),rule15)
    gerd_severe_result = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(
        rule16, rule17), rule18), rule19), rule20), rule21), rule22), rule23), rule24), rule25), rule26), rule27), rule28), rule29), rule30)
    gerd_moderate_result = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(
        rule31, rule32), rule33), rule34), rule35), rule36), rule37), rule38), rule39), rule40), rule41), rule42), rule43), rule44)
    gerd_mild_result = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(
        rule45, rule46), rule47), rule48), rule49), rule50), rule51), rule52), rule53), rule54), rule55), rule56), rule57)
    gerd_very_mild_result  = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(
        rule58,rule59),rule60),rule61),rule62),rule63),rule64),rule65),rule66),rule67),rule68),rule69),rule70)


    # In[32]:


    # Output grafik
    risk0 = np.zeros_like(gerd_range)


    # In[33]:


    # Kalkulasi hasil akhir GERD berdasarkan rules dan lakukan defuzzyfication
    gerd_result = np.fmax(np.fmax(np.fmax(np.fmax(gerd_very_mild_result, gerd_mild_result), gerd_moderate_result), gerd_severe_result), gerd_very_severe_result)

    defuzzified  = fuzz.defuzz(gerd_range, gerd_result, 'centroid')

    result = fuzz.interp_membership(gerd_range, gerd_result, defuzzified)

    # Defuzzification Centroid Diagram
    fig, ax0 = plt.subplots(figsize=(7, 4))

    ax0.plot(gerd_range, gerd_very_mild, 'r', linewidth = 0.5, linestyle = '--')
    ax0.plot(gerd_range, gerd_mild, 'g', linewidth = 0.5, linestyle = '--')
    ax0.plot(gerd_range, gerd_moderate, 'b', linewidth = 0.5, linestyle = '--')
    ax0.plot(gerd_range, gerd_severe, 'y', linewidth = 0.5, linestyle = '--')
    ax0.plot(gerd_range, gerd_very_severe, 'm', linewidth = 0.5, linestyle = '--')

    ax0.fill_between(gerd_range, risk0, gerd_result, facecolor = 'red', alpha = 0.7)
    ax0.plot([defuzzified , defuzzified], [0, result], 'k', linewidth = 1.5, alpha = 0.9)
    ax0.set_title('GERD Defuzzification Result')

    #save graphic ke png
    fig.savefig('static/tabel_akhir.png')

    plt.tight_layout()


    # In[34]:
    # Print hasil akhir gerd
    # Dikali 10 agar bentuknya persentase
    return defuzzified*10

