using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System.Threading.Tasks;
using System.Drawing;
using UnityEngine.UI;
using static Unity.VisualScripting.Metadata;

public class GameManager: MonoBehaviour
{
    public static GameManager instance;
    public string gameStatus = "TITLE";
    public int dimension;
    public int size;
    public string focusblock_Status="interval";
    /*
    hold:ブロックを落とす前
    fall:落下中
    interval:次に生成されるまで
    */

    public int generate_height;
    private int area_x;
    private int area_z;
    public const int area_y = 20;
    public int half_width;

    public GameObject[] blockPrefabs; 
    public GameObject FlatPrefab;
    public GameObject limit_bar;
    public GameObject block_parent;
    public Text scoreText;
    public Text infoText;
    public Text titleText;
    public Image settingPanel;
    public Button button2;
    public Button button3;
    public Image check2;
    public Image check3;
    public GameObject []mino_Image;

    public int[,,] blockarea;

    private bool display_settingPanel = false;
    private float generate_interval;
    public float generate_count;
    public int hold_id = -1;
    public float  fall_interval;
    private float gamescore = 0f;
    private float maxheight = 0f;
    private int mino_count = 0;

    // Start is called before the first frame update
    void Start()
    {
        instance = this;
        gameStatus = "TITLE";
        size = 9;
        settingPanel.gameObject.SetActive(false);
        check2.gameObject.SetActive(false);
        generate_interval = 0.5f;
        button2.onClick.AddListener(ToggleD);
        button3.onClick.AddListener(ToggleD);
        display_score(0);
        foreach(GameObject obj in mino_Image)
            obj.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        if(gameStatus == "TITLE")
        {
            if (Input.GetKeyDown(KeyCode.Space))
            {
                //infoText.text = "";
                //titleText.text = "";
                setStage(dimension);
                gameStatus = "PLAY";
                
                settingPanel.gameObject.SetActive(false);
                display_score(0);
            }

            if (Input.GetKeyDown(KeyCode.E))
            {
                if (display_settingPanel)
                {
                    settingPanel.gameObject.SetActive(false);
                    display_settingPanel = false;
                }
                else
                {
                    settingPanel.gameObject.SetActive(true);
                    display_settingPanel= true;
                }
            }
            
        }

        if(gameStatus == "PLAY")
        {
            if (focusblock_Status == "interval")
            {
                if (generate_count < 0f)
                {
                    int[] arr = judge_();
                    //string s = "";
                    //foreach(int i in arr)
                    //{
                    //    s += i;
                    //}
                    //print(s);
                    int count = 0;

                    for (int i = 0; i < arr.Length; i++)
                    {
                        if (arr[i] == 1)
                        {
                            count++;
                        }
                        else
                        {
                            if (count > 0)
                            {
                                display_score(count);
                                count = 0;
                            }
                        }
                    }
                    if (count > 0)
                    {
                        display_score(count);
                    }
                    if (mino_count % 10 == 0) fall_interval *= 0.8f;                    int rand = Random.Range(0, blockPrefabs.Length);
                    //rand = 1;
                    GameObject genarate_block = Instantiate(blockPrefabs[rand]);
                    genarate_block.transform.position = new Vector3(0f, generate_height+maxheight, 0f);
                    mino_count++;
                    generate_count = generate_interval;
                    array_out();
                    focusblock_Status = "hold";
                    Transform[] children = block_parent.GetComponentsInChildren<Transform>();
                    maxheight = 0f;
                    foreach(Transform child in children)
                    {
                        if(child.transform.position.y > maxheight)
                        {
                            maxheight = child.transform.position.y;
                        }
                    }
                    //PlayerController.instance.change_pos(maxheight);
                }
                else
                {
                    generate_count -= Time.deltaTime;
                }
            }
        }
        
    }

    public void setStage(int dimension)
    {
        if(dimension == 2)
        {
            GameObject Flat = Instantiate(FlatPrefab);
            Flat.transform.localScale = new Vector3(size, Flat.transform.localScale.y, 1f);
            area_x = size;
            area_z = 1;

            blockarea = new int[area_z, area_y, area_x];
            for (int i = 0; i < area_z; i++)
                for (int j = 0; j < area_x; j++)
                    for (int k = 0; k < area_y; k++)
                        blockarea[i, k, j] = 0;

            half_width = (int)((area_x - 1) / 2);

            //limit_barの生成
            GameObject left = Instantiate(limit_bar);
            left.transform.position = new Vector3(-(half_width + 1.2f), 15f, 0f);
            GameObject right = Instantiate(limit_bar);
            right.transform.position = new Vector3(half_width + 1.2f, 15f, 0f);
            GameObject front = Instantiate(limit_bar);
            front.transform.position = new Vector3(0f, 15f, 1.2f);
            front.transform.localScale = new Vector3(half_width * 2f + 1f, 30f, 1f);
            GameObject back = Instantiate(limit_bar);
            back.transform.position = new Vector3(0f, 15f, -1.2f);
            back.transform.localScale = new Vector3(half_width * 2f + 1f, 30f, 1f);

            GameObject parent = GameObject.FindWithTag("limit_bar_parent");
            left.transform.SetParent(parent.transform);
            right.transform.SetParent(parent.transform);
            front.transform.SetParent(parent.transform);
            back.transform.SetParent(parent.transform);
        }

        else if(dimension == 3)
        {
            GameObject Flat = Instantiate(FlatPrefab);
            Flat.transform.localScale = new Vector3(size, Flat.transform.localScale.y, size);
            area_x = size;
            area_z = size;
            

            blockarea = new int[area_x, area_y, area_z];
            for (int i = 0; i < area_x; i++)
                for (int j = 0; j < area_z; j++)
                    for (int k = 0; k < area_y; k++)
                        blockarea[i, k, j] = 0;
            half_width = (int)((area_x - 1) / 2);

            //limit_barの生成
            GameObject left = Instantiate(limit_bar);
            left.transform.position = new Vector3(0f, 15f, -(half_width + 1.2f));
            left.transform.localScale = new Vector3(half_width * 2f + 1f, 30f, 1f);
            GameObject right = Instantiate(limit_bar);
            right.transform.position = new Vector3(0f, 15f, half_width + 1.2f);
            right.transform.localScale = new Vector3(half_width * 2f + 1f, 30f, 1f);
            GameObject front = Instantiate(limit_bar);
            front.transform.position = new Vector3(half_width + 1.2f, 15f, 0f);
            front.transform.localScale = new Vector3(1f, 30f, half_width * 2f + 1f);
            GameObject back = Instantiate(limit_bar);
            back.transform.position = new Vector3(-(half_width + 1.2f), 15f, 0f);
            back.transform.localScale = new Vector3(1f, 30f, half_width * 2f + 1f);
            GameObject parent = GameObject.FindWithTag("limit_bar_parent");
            left.transform.SetParent(parent.transform);
            right.transform.SetParent(parent.transform);
            front.transform.SetParent(parent.transform);
            back.transform.SetParent(parent.transform);
        }
    }

    public void Change_blockArray(Vector3 pos)
    {
        int x, y, z;

        x = (int)(pos[0] + half_width + 0.5);
        y = (int)(pos[1] + 0.5);
        z = (int)(pos[2] + half_width + 0.5);
        if (dimension == 2) z = 0;
        //print($"in_method:{x}, {y}, {z}");
        blockarea[z, y, x] = 1;
    }

    //外部ファイルに現状のステージを出力
    private void array_out()
    {
        string filePath = "output.txt";  // 出力するファイルのパス
        string row = "";
        using (StreamWriter writer = new StreamWriter(filePath, false))
        {
            for (int _y = 0; _y < area_y; _y++)  // 層のループ
            {
                row += $"{_y}段目:\n";
                for (int _x = 0; _x < area_x; _x++)  // 行のループ
                {

                    for (int _z = 0; _z < area_z; _z++)  // 列のループ
                    {
                        if(dimension == 2) _z = 0;
                        row += blockarea[_z, _y, _x] + " ";  // 行の要素を結合
                    }
                }

                row += "\n";
                writer.WriteLine(row);
            }
        }
        System.Console.WriteLine();
    }

    private int[] judge_()
    {
        print("in_judge");
        int[] fall_hegiht = new int[area_y];    //i層をどれだけ落とすかを記録
        int[] sum = new int[area_y];
        int result = 0;
        int[] res = new int[area_y];    //i層が破壊されたかどうかを記録，1ならi層が破壊された
        //結果記録配列の初期化
        for (int i = 0; i < fall_hegiht.Length; i++){
            fall_hegiht[i] = 0;
        }
        for(int i = 0; i < res.Length; i++)
        {
            res[i] = 0;
        }
        //各層がすべてブロックで埋まったかを確認し，破壊
        for(int i = 0; i < area_y; i++)
        {
            sum[i] = 0;
            
            for (int j = 0; j < area_x; j++)
            {
                for (int k = 0; k < area_z; k++)
                {
                    if(dimension == 2) k = 0;
                    sum[i] += blockarea[k, i, j];
                }
            }
            
            if (sum[i] == area_x * area_z)
            {
                print($"{i}段目破壊");
                res[i]++;
                DestroyLayer(i);
                result += 1;
                for(int j=i+1; j < area_y; j++)
                {
                    fall_hegiht[j] += 1;
                }
                fall_hegiht[i] = 0;
            }
        }
        //1層以上破壊されていた場合に落とす
        if (result != 0)
            stuff_bottom(fall_hegiht);
        
        return res;
    }

    private void DestroyLayer(int _y)
    {
        float y = (float)_y;
        
        for (int i = 0; i < area_z; i++)
        {

            int temp_i = i;
            if (dimension == 3) temp_i -= half_width;
            for (int j = 0; j < area_x; j++)
            {
                int temp_j = j -  half_width;
                Vector3 targetPos = new Vector3(temp_j, y, temp_i);
                //print(targetPos);
                Collider[] colliders = Physics.OverlapSphere(targetPos, 0.1f);
                print(colliders.Length);
                foreach (Collider collider in colliders)
                {
                    Destroy(collider.gameObject);
                }
            }
        }
        for(int i = 0; i < area_z; i++)
        {
            for(int j=0; j < area_x; j++)
            {
                blockarea[i, _y, j] = 0;
            }
        }

    }

   private void stuff_bottom(int[] _y)
    {
        //print("in_stuff_bottom");
        GameObject[] blockArray = GameObject.FindGameObjectsWithTag("flat"); 
        int len = blockArray.Length;
        print($"存在するblockの個数:{len-1}");
        for(int i = 1;i< area_y; i++)
        {
            GameObject[] ls = new GameObject[len];
            //y座標ごとのブロックを配列に格納
            int k = 0;
            foreach(GameObject g in blockArray)
            {
                //print($"g:{g.transform.position.y}, i:{(float)i}");
                if(g.transform.position.y >(float)(i-0.5) && g.transform.position.y < (float)(i+0.5))
                {
                    ls[k] = g;
                }
                k++;
            }

            //ブロック消えた分下げる
            foreach(GameObject g in ls)
            {
                if(g != null)
                {
                    Vector3 pos = g.transform.position;
                    pos.y -= _y[i];
                    g.transform.position = pos;
                }
            }

            //blockArrayを消えたぶん下げる
            for(int j=0;j<area_z; j++)
            {
                for(int l=0;l<area_x; l++)
                {
                    blockarea[j, i - _y[i], l] = blockarea[j, i, l];
                }
            }
        }
    }

    public void change_hold(int id, float y)
    {
        int rand = hold_id;
        if(hold_id == -1) rand = Random.Range(0, blockPrefabs.Length);
        display_hold(hold_id, id);
        hold_id = id;
        GameObject genarate_block = Instantiate(blockPrefabs[rand]);
        genarate_block.transform.position = new Vector3(0f, y, 0f);

    }

    public void display_hold(int pre_id, int after_id)
    {
        if(pre_id!=-1)mino_Image[pre_id].SetActive(false);
        mino_Image[after_id].SetActive(true);
    }

    private void display_score(int num)
    {
        float temp_score = 0f;
        if (num == 1)
        {
            temp_score = 100f;
        }
        else if (num == 2)
        {
            temp_score = 220f;
        }
        else if (num == 3)
        {
            temp_score = 360f;
        }
        else if (num == 4)
        {
            print("tetris!");
            temp_score = 500f;
        }
        gamescore += temp_score;
        scoreText.text = gamescore.ToString("00.0");
    }

    private void ToggleD()
    {
        if (dimension == 2)
            dimension = 3;
        else if (dimension == 3)
            dimension = 2;
        UpdateUI();
    }

    private void UpdateUI()
    {
        bool is2D = (dimension == 2);

        check2.gameObject.SetActive(is2D);
        check3.gameObject.SetActive(!is2D);

    }
}
