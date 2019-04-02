import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class KMeans{

HashMap<String, List<Integer>> cluster_permission_matrix = new HashMap<String, List<Integer>>();

KMeans()
{
cluster_permission_matrix.put("ADRD",new ArrayList<>(Arrays.asList(1,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("AnserverBot",new ArrayList<>(Arrays.asList(1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0)));
cluster_permission_matrix.put("BaseBridge",new ArrayList<>(Arrays.asList(1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("BeanBot",new ArrayList<>(Arrays.asList(1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Bgserv",new ArrayList<>(Arrays.asList(1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0)));
cluster_permission_matrix.put("CoinPirate",new ArrayList<>(Arrays.asList(1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0)));
cluster_permission_matrix.put("CruseWin",new ArrayList<>(Arrays.asList(1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DogWars",new ArrayList<>(Arrays.asList(1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidCoupon",new ArrayList<>(Arrays.asList(1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidDeluxe",new ArrayList<>(Arrays.asList(1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidDreamLight",new ArrayList<>(Arrays.asList(1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidDream",new ArrayList<>(Arrays.asList(1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidKungFu1",new ArrayList<>(Arrays.asList(1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidKungFu2",new ArrayList<>(Arrays.asList(1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidKungFu3",new ArrayList<>(Arrays.asList(1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidKungFu4",new ArrayList<>(Arrays.asList(1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("DroidKungFuUpdate",new ArrayList<>(Arrays.asList(1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Endofday",new ArrayList<>(Arrays.asList(1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("FakeNetflix",new ArrayList<>(Arrays.asList(1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("FakePlayer",new ArrayList<>(Arrays.asList(0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("GGTracker",new ArrayList<>(Arrays.asList(1,1,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0)));
cluster_permission_matrix.put("GPSSMSSpy/FakePlayer/SMSReplicator",new ArrayList<>(Arrays.asList(0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("GamblerSMS",new ArrayList<>(Arrays.asList(1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0)));
cluster_permission_matrix.put("Geinimi",new ArrayList<>(Arrays.asList(1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("GingerMaster",new ArrayList<>(Arrays.asList(1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0)));
cluster_permission_matrix.put("GoldDream",new ArrayList<>(Arrays.asList(1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Gone60",new ArrayList<>(Arrays.asList(1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("HippoSMS",new ArrayList<>(Arrays.asList(1,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Jifake",new ArrayList<>(Arrays.asList(1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("KMin",new ArrayList<>(Arrays.asList(1,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("LoveTrap",new ArrayList<>(Arrays.asList(1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("NickyBot",new ArrayList<>(Arrays.asList(1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0)));
cluster_permission_matrix.put("NickySpy",new ArrayList<>(Arrays.asList(1,0,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0)));
cluster_permission_matrix.put("Pjapps",new ArrayList<>(Arrays.asList(1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Plankton",new ArrayList<>(Arrays.asList(1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("RogueLemon",new ArrayList<>(Arrays.asList(1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("RogueSPPush",new ArrayList<>(Arrays.asList(1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("SndApps",new ArrayList<>(Arrays.asList(1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Spitmo",new ArrayList<>(Arrays.asList(1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Tapsnake",new ArrayList<>(Arrays.asList(1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Walkinwat",new ArrayList<>(Arrays.asList(1,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("YZHC",new ArrayList<>(Arrays.asList(1,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Zitmo",new ArrayList<>(Arrays.asList(1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("Zsone",new ArrayList<>(Arrays.asList(1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0)));
cluster_permission_matrix.put("jSMSHider",new ArrayList<>(Arrays.asList(1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)));
cluster_permission_matrix.put("zHash",new ArrayList<>(Arrays.asList(1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0)));
}

public String find_cluster(int[] perm_list)
{
    int number_of_permission = 24;
    int similarity_score = 0;
    int disimilarity_score = 0;
    String cluster_name = "";
    for (String family_name :cluster_permission_matrix.keySet())
    {
        // System.out.println(family_name);
        int cluster_vector[] =  convertIntegers(cluster_permission_matrix.get(family_name));
        int temp_sim_score = 0;
        int temp_dis_score = 0;
        
        for(int i = 0 ; i < number_of_permission ; i++)
        {
            if(perm_list[i] == cluster_vector[i])
            {
               if(perm_list[i] == 1)
               {
                    temp_sim_score++;
               }
            }
            else
            {
                temp_dis_score++;
            }
        
        if(temp_sim_score > similarity_score)
        {

            similarity_score = temp_sim_score;
            disimilarity_score = temp_dis_score;
            cluster_name = family_name;
        }
        else if(temp_sim_score ==  similarity_score)
        {
            if(disimilarity_score > temp_dis_score)
            {
                disimilarity_score = temp_dis_score;
                cluster_name = family_name;
            }
        }
        }

    }
    return cluster_name;
}


public static int[] convertIntegers(List<Integer> integers)
{
    int[] ret = new int[integers.size()];
    for (int i=0; i < ret.length; i++)
    {
        ret[i] = integers.get(i).intValue();
    }
    return ret;
}

public static void main(String[] args) {
    
    KMeans k = new KMeans();
    int[] perm_vector = new int[]{1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    System.out.println(k.find_cluster(perm_vector));
}
}
