from datetime import datetime, timedelta
from calendar import monthrange

def trie_genre(data):
    
    H_data = []
    F_data = []
    
    for line in data:
        if line['genre'] == 'Masculin':
            H_data.append(line)
        else:
            F_data.append(line)
    
    return {"Homme": H_data, "Femme": F_data}



def trie_post(data):
    
    Tuberculose_data = []
    CPN2_Acccouch_CPoN_data = []
    IST_data = []
    Hospitalisation_data = []
    Index_testing_data = []
    Urgence_data = []
    Malnutrition_data = []
    Autre_CDIP_data = []
    
    for line in data:
        
        if line['post_de_depistage'] == 'Tuberculose':
            Tuberculose_data.append(line)
            
        elif line['post_de_depistage'] == 'CPN2 et Plus + Acccouch + CPoN':
            CPN2_Acccouch_CPoN_data.append(line)
            
        elif line['post_de_depistage'] == 'IST':
            IST_data.append(line)
            
        elif line['post_de_depistage'] == 'Hospitalisation':
            Hospitalisation_data.append(line)
            
        elif line['post_de_depistage'] == 'Index testing':
            Index_testing_data.append(line)
            
        elif line['post_de_depistage'] == 'Urgence':
            Urgence_data.append(line)
            
        elif line['post_de_depistage'] == 'Malnutrition':
            Malnutrition_data.append(line)
            
        else:
            Autre_CDIP_data.append(line)
    
    return {'Tuberculose': Tuberculose_data, 'CPN2 et Plus + Acccouch + CPoN': CPN2_Acccouch_CPoN_data,
           'IST':IST_data, 'Hospitalisation': Hospitalisation_data, 'Index testing':Index_testing_data,
           'Urgence':Urgence_data, 'Malnutrition': Malnutrition_data, 'Autre CDIP': Autre_CDIP_data}




def decompte(data, propriete):
    
    conseiller = [0]*12
    depister = [0]*12
    conseiller_depister = [0]*12
    postif = [0]*12
    resultat_recu = [0]*12
    beneficiant_CD4 = [0]*12
    negatif = [0]*12
    
    if propriete == 'conseiller':
        for line in data:
            if line["age"]<1:
                conseiller[0] = conseiller[0] + int(line['conseiller'] == "OUI")
            
            elif line["age"]>=1 and line["age"]<=4:
                conseiller[1] = conseiller[1] + int(line['conseiller'] == "OUI")
                
            elif line["age"]>=5 and line["age"]<=9:
                conseiller[2] = conseiller[2] + int(line['conseiller'] == "OUI")
                
            elif line["age"]>=10 and line["age"]<=14:
                conseiller[3] = conseiller[3] + int(line['conseiller'] == "OUI")
                
            elif line["age"]>=15 and line["age"]<=19:
                conseiller[4] = conseiller[4] + int(line['conseiller'] == "OUI")
                
            elif line["age"]>=20 and line["age"]<=24:
                conseiller[5] = conseiller[5] + int(line['conseiller'] == "OUI")
                
            elif line["age"]>=25 and line["age"]<=29:
                conseiller[6] = conseiller[6] + int(line['conseiller'] == "OUI")
                
            elif line["age"]>=30 and line["age"]<=34:
                conseiller[7] = conseiller[7] + int(line['conseiller'] == "OUI")
                
            elif line["age"]>=35 and line["age"]<=39:
                conseiller[8] = conseiller[8] + int(line['conseiller'] == "OUI")     
               
            elif line["age"]>=40 and line["age"]<=44:
                conseiller[9] = conseiller[9] + int(line['conseiller'] == "OUI")
                
            elif line["age"]>=45 and line["age"]<=49:
                conseiller[10] = conseiller[10] + int(line['conseiller'] == "OUI")
                
            else:
                conseiller[11] = conseiller[11] + int(line['conseiller'] == "OUI")
        
        return conseiller
    
    
    if propriete == 'depister':
        for line in data:
            if line["age"]<1:
                depister[0] = depister[0] + int(line['depister'] == "OUI")
            
            elif line["age"]>=1 and line["age"]<=4:
                depister[1] = depister[1] + int(line['depister'] == "OUI")
                
            elif line["age"]>=5 and line["age"]<=9:
                depister[2] = depister[2] + int(line['depister'] == "OUI")
                
            elif line["age"]>=10 and line["age"]<=14:
                depister[3] = depister[3] + int(line['depister'] == "OUI")
                
            elif line["age"]>=15 and line["age"]<=19:
                depister[4] = depister[4] + int(line['depister'] == "OUI")
                
            elif line["age"]>=20 and line["age"]<=24:
                depister[5] = depister[5] + int(line['depister'] == "OUI")
                
            elif line["age"]>=25 and line["age"]<=29:
                depister[6] = depister[6] + int(line['depister'] == "OUI")
                
            elif line["age"]>=30 and line["age"]<=34:
                depister[7] = depister[7] + int(line['depister'] == "OUI")
                
            elif line["age"]>=35 and line["age"]<=39:
                depister[8] = depister[8] + int(line['depister'] == "OUI")     
               
            elif line["age"]>=40 and line["age"]<=44:
                depister[9] = depister[9] + int(line['depister'] == "OUI")
                
            elif line["age"]>=45 and line["age"]<=49:
                depister[10] = depister[10] + int(line['depister'] == "OUI")
                
            else:
                depister[11] = depister[11] + int(line['depister'] == "OUI")
        
        return depister
    
    
    
    if propriete == 'conseiller_depister':
        for line in data:
            if line["age"]<1:
                conseiller_depister[0] = conseiller_depister[0] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
            
            elif line["age"]>=1 and line["age"]<=4:
                conseiller_depister[1] = conseiller_depister[1] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            elif line["age"]>=5 and line["age"]<=9:
                conseiller_depister[2] = conseiller_depister[2] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            elif line["age"]>=10 and line["age"]<=14:
                conseiller_depister[3] = conseiller_depister[3] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            elif line["age"]>=15 and line["age"]<=19:
                conseiller_depister[4] = conseiller_depister[4] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            elif line["age"]>=20 and line["age"]<=24:
                conseiller_depister[5] = conseiller_depister[5] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            elif line["age"]>=25 and line["age"]<=29:
                conseiller_depister[6] = conseiller_depister[6] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            elif line["age"]>=30 and line["age"]<=34:
                conseiller_depister[7] = conseiller_depister[7] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            elif line["age"]>=35 and line["age"]<=39:
                conseiller_depister[8] = conseiller_depister[8] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")     
               
            elif line["age"]>=40 and line["age"]<=44:
                conseiller_depister[9] = conseiller_depister[9] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            elif line["age"]>=45 and line["age"]<=49:
                conseiller_depister[10] = conseiller_depister[10] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
                
            else:
                conseiller_depister[11] = conseiller_depister[11] + int(line['conseiller'] == "OUI" and line['depister'] == "OUI")
        
        return conseiller_depister
    
    
    
    if propriete == 'resultat_recu':
        for line in data:
            if line["age"]<1:
                resultat_recu[0] = resultat_recu[0] + int(line['resultat_recu'] == "OUI")
            
            elif line["age"]>=1 and line["age"]<=4:
                resultat_recu[1] = resultat_recu[1] + int(line['resultat_recu'] == "OUI")
                
            elif line["age"]>=5 and line["age"]<=9:
                resultat_recu[2] = resultat_recu[2] + int(line['resultat_recu'] == "OUI")
                
            elif line["age"]>=10 and line["age"]<=14:
                resultat_recu[3] = resultat_recu[3] + int(line['resultat_recu'] == "OUI")
                
            elif line["age"]>=15 and line["age"]<=19:
                resultat_recu[4] = resultat_recu[4] + int(line['resultat_recu'] == "OUI")
                
            elif line["age"]>=20 and line["age"]<=24:
                resultat_recu[5] = resultat_recu[5] + int(line['resultat_recu'] == "OUI")
                
            elif line["age"]>=25 and line["age"]<=29:
                resultat_recu[6] = resultat_recu[6] + int(line['resultat_recu'] == "OUI")
                
            elif line["age"]>=30 and line["age"]<=34:
                resultat_recu[7] = resultat_recu[7] + int(line['resultat_recu'] == "OUI")
                
            elif line["age"]>=35 and line["age"]<=39:
                resultat_recu[8] = resultat_recu[8] + int(line['resultat_recu'] == "OUI")     
               
            elif line["age"]>=40 and line["age"]<=44:
                resultat_recu[9] = resultat_recu[9] + int(line['resultat_recu'] == "OUI")
                
            elif line["age"]>=45 and line["age"]<=49:
                resultat_recu[10] = resultat_recu[10] + int(line['resultat_recu'] == "OUI")
                
            else:
                resultat_recu[11] = resultat_recu[11] + int(line['resultat_recu'] == "OUI")
        
        return resultat_recu
    
    
    if propriete == 'beneficiant_CD4':
        for line in data:
            if line["age"]<1:
                beneficiant_CD4[0] = beneficiant_CD4[0] + int(line['beneficiant_CD4'] == "OUI")
            
            elif line["age"]>=1 and line["age"]<=4:
                beneficiant_CD4[1] = beneficiant_CD4[1] + int(line['beneficiant_CD4'] == "OUI")
                
            elif line["age"]>=5 and line["age"]<=9:
                beneficiant_CD4[2] = beneficiant_CD4[2] + int(line['beneficiant_CD4'] == "OUI")
                
            elif line["age"]>=10 and line["age"]<=14:
                beneficiant_CD4[3] = beneficiant_CD4[3] + int(line['beneficiant_CD4'] == "OUI")
                
            elif line["age"]>=15 and line["age"]<=19:
                beneficiant_CD4[4] = beneficiant_CD4[4] + int(line['beneficiant_CD4'] == "OUI")
                
            elif line["age"]>=20 and line["age"]<=24:
                beneficiant_CD4[5] = beneficiant_CD4[5] + int(line['beneficiant_CD4'] == "OUI")
                
            elif line["age"]>=25 and line["age"]<=29:
                beneficiant_CD4[6] = beneficiant_CD4[6] + int(line['beneficiant_CD4'] == "OUI")
                
            elif line["age"]>=30 and line["age"]<=34:
                beneficiant_CD4[7] = beneficiant_CD4[7] + int(line['beneficiant_CD4'] == "OUI")
                
            elif line["age"]>=35 and line["age"]<=39:
                beneficiant_CD4[8] = beneficiant_CD4[8] + int(line['beneficiant_CD4'] == "OUI")     
               
            elif line["age"]>=40 and line["age"]<=44:
                beneficiant_CD4[9] = beneficiant_CD4[9] + int(line['beneficiant_CD4'] == "OUI")
                
            elif line["age"]>=45 and line["age"]<=49:
                beneficiant_CD4[10] = beneficiant_CD4[10] + int(line['beneficiant_CD4'] == "OUI")
                
            else:
                beneficiant_CD4[11] = beneficiant_CD4[11] + int(line['beneficiant_CD4'] == "OUI")
        
        return beneficiant_CD4
    
    
    if propriete == 'postif':
        for line in data:
            if line["age"]<1:
                postif[0] = postif[0] + int(line['resultat'] == "Positif")
            
            elif line["age"]>=1 and line["age"]<=4:
                postif[1] = postif[1] + int(line['resultat'] == "Positif")
                
            elif line["age"]>=5 and line["age"]<=9:
                postif[2] = postif[2] + int(line['resultat'] == "Positif")
                
            elif line["age"]>=10 and line["age"]<=14:
                postif[3] = postif[3] + int(line['resultat'] == "Positif")
                
            elif line["age"]>=15 and line["age"]<=19:
                postif[4] = postif[4] + int(line['resultat'] == "Positif")
                
            elif line["age"]>=20 and line["age"]<=24:
                postif[5] = postif[5] + int(line['resultat'] == "Positif")
                
            elif line["age"]>=25 and line["age"]<=29:
                postif[6] = postif[6] + int(line['resultat'] == "Positif")
                
            elif line["age"]>=30 and line["age"]<=34:
                postif[7] = postif[7] + int(line['resultat'] == "Positif")
                
            elif line["age"]>=35 and line["age"]<=39:
                postif[8] = postif[8] + int(line['resultat'] == "Positif")     
               
            elif line["age"]>=40 and line["age"]<=44:
                postif[9] = postif[9] + int(line['resultat'] == "Positif")
                
            elif line["age"]>=45 and line["age"]<=49:
                postif[10] = postif[10] + int(line['resultat'] == "Positif")
                
            else:
                postif[11] = postif[11] + int(line['resultat'] == "Positif")
        
        return postif
    
    
    if propriete == 'negatif':
        for line in data:
            if line["age"]<1:
                negatif[0] = negatif[0] + int(line['resultat'] == "Négatif")
            
            elif line["age"]>=1 and line["age"]<=4:
                negatif[1] = negatif[1] + int(line['resultat'] == "Négatif")
                
            elif line["age"]>=5 and line["age"]<=9:
                negatif[2] = negatif[2] + int(line['resultat'] == "Négatif")
                
            elif line["age"]>=10 and line["age"]<=14:
                negatif[3] = negatif[3] + int(line['resultat'] == "Négatif")
                
            elif line["age"]>=15 and line["age"]<=19:
                negatif[4] = negatif[4] + int(line['resultat'] == "Négatif")
                
            elif line["age"]>=20 and line["age"]<=24:
                negatif[5] = negatif[5] + int(line['resultat'] == "Négatif")
                
            elif line["age"]>=25 and line["age"]<=29:
                negatif[6] = negatif[6] + int(line['resultat'] == "Négatif")
                
            elif line["age"]>=30 and line["age"]<=34:
                negatif[7] = negatif[7] + int(line['resultat'] == "Négatif")
                
            elif line["age"]>=35 and line["age"]<=39:
                negatif[8] = negatif[8] + int(line['resultat'] == "Négatif")     
               
            elif line["age"]>=40 and line["age"]<=44:
                negatif[9] = negatif[9] + int(line['resultat'] == "Négatif")
                
            elif line["age"]>=45 and line["age"]<=49:
                negatif[10] = negatif[10] + int(line['resultat'] == "Négatif")
                
            else:
                negatif[11] = negatif[11] + int(line['resultat'] == "Négatif")
        
        return negatif



def data_traitee(data):

    posts = ('Tuberculose', 'CPN2 et Plus + Acccouch + CPoN', 'IST', 'Hospitalisation', 'Index testing',
                    'Urgence', 'Malnutrition', 'Autre CDIP')

    final_data = {}

    for post in posts:

        final_data[post] = []

        data_post = trie_post(data)[post]

        val_conseiller = decompte(trie_genre(data_post)["Homme"], "conseiller")
        val_conseiller.extend(decompte(trie_genre(data_post)["Femme"], "conseiller"))
        val_conseiller.append(sum(val_conseiller))

        val_depister = decompte(trie_genre(data_post)["Homme"], "depister")
        val_depister.extend(decompte(trie_genre(data_post)["Femme"], "depister"))
        val_depister.append(sum(val_depister))

        val_conseiller_depister = decompte(trie_genre(data_post)["Homme"], "conseiller_depister")
        val_conseiller_depister.extend(decompte(trie_genre(data_post)["Femme"], "conseiller_depister"))
        val_conseiller_depister.append(sum(val_conseiller_depister))

        val_postif = decompte(trie_genre(data_post)["Homme"], "postif")
        val_postif.extend(decompte(trie_genre(data_post)["Femme"], "postif"))
        val_postif.append(sum(val_postif))

        val_resultat_recu = decompte(trie_genre(data_post)["Homme"], "resultat_recu")
        val_resultat_recu.extend(decompte(trie_genre(data_post)["Femme"], "resultat_recu"))
        val_resultat_recu.append(sum(val_resultat_recu))

        val_beneficiant_CD4 = decompte(trie_genre(data_post)["Homme"], "beneficiant_CD4")
        val_beneficiant_CD4.extend(decompte(trie_genre(data_post)["Femme"], "beneficiant_CD4"))
        val_beneficiant_CD4.append(sum(val_beneficiant_CD4))

        val_negatif = decompte(trie_genre(data_post)["Homme"], "negatif")
        val_negatif.extend(decompte(trie_genre(data_post)["Femme"], "negatif"))
        val_negatif.append(sum(val_negatif))

        final_data[post].extend([val_conseiller, val_depister, val_conseiller_depister, val_postif, 
                                 val_resultat_recu, val_beneficiant_CD4, val_negatif])

    return final_data


def afficher_mois(cle):

    mois = {
        0: 'Décembre',
        1: 'Janvier',
        2: 'Février',
        3: 'Mars',
        4: 'Avril',
        5: 'Mai',
        6: 'Juin',
        7: 'Juillet',
        8: 'Août',
        9: 'Septembre',
        10: 'Octobre',
        11: 'Novembre',
        12: 'Décembre'
    }

    return mois[cle]




def monthdelta(d1, d2):

    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    # use with df['months_difference'] = df[['date1', 'date2']].apply(monthdelta, axis=1)
    return delta + 1