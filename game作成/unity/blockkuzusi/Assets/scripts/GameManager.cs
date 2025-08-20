using UnityEngine;
using UnityEngine.UI;
using System;
using System.IO;
using System.Net.NetworkInformation;


public class GameManager : MonoBehaviour
{
    public static GameManager instance;

    public GameObject[] blockPrefabs;
    public GameObject ballPrefab;
    public GameObject ironPrefab;
    public GameObject[] ItemPrefabs;
    public Text titleText;
    public Text timerText;

    public string gameStatus;
    private int level;

    private int width_x = 15;
    private int width_y = 5;
    private int height_y = 11;
    public int block_count = 0;
    private Vector3 pos_bar;
    private float countTimer;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        instance = this;
        gameStatus = "TITLE";
        GameObject bar = GameObject.FindWithTag("bar");
        pos_bar = bar.transform.position;
        level = 1;
        countTimer = 60f;
    }

    // Update is called once per frame
    void Update()
    {
        if(gameStatus == "TITLE")
        {
            if(Input.GetKeyDown(KeyCode.Escape))
            {
                titleText.text = "";
                SetnewLevel(level);
            }
        }
        else if (gameStatus == "PLAY")
        {
            if(block_count == 0)
            {
                gameStatus = "CLEAR";
                titleText.text = "CLEAR!!!\nLet's Next Level\nHit Enter Key";
            }

            if (countTimer > 0f)
            {
                countTimer -= Time.deltaTime;

            }
            else
            {
                gameStatus = "GAMEOVER";
            }
            if(countTimer < 10f)
            {
                timerText.color = Color.red;
            }
            timerText.text = countTimer.ToString("000.0");
        }
        else if (gameStatus == "GAMEOVER")
        {
            titleText.text = "GAME OVER";
        }
        else if(gameStatus == "CLEAR")
        {
            if(Input.GetKey(KeyCode.Return))
            {
                level++;
                countTimer = 60f;
                SetnewLevel(level);
            }
        }
    }

    private void SetnewLevel(int l)
    {
        SetBlock(l);
        SetIron();
        gameStatus = "PLAY";
        Vector3 pos = pos_bar;
        pos.y += 5f;
        GameObject obj = Instantiate(ballPrefab);
        obj.transform.position = pos;
    }

    private void SetBlock(int l)
    {
        string filePath = "Assets/stage_text/" + l + ".txt";
        string s = File.ReadAllText(filePath);
        print(s);

        int x = -(width_x - 1)/2;
        int y = width_y;
        foreach (char t in s)
        {
            //print(t);
            if(t == '*')
            {
                GameObject obj = Instantiate(blockPrefabs[0]);
                obj.GetComponent<Renderer>().material.color = UnityEngine.Random.ColorHSV();
                obj.transform.position = new Vector3(x, height_y + y, 0);
                block_count++;
                x += 1;
            }
            else if(t == '-')
            {
                GameObject obj = Instantiate(blockPrefabs[1]);
                obj.GetComponent<Renderer>().material.color = UnityEngine.Random.ColorHSV();
                obj.transform.position = new Vector3(x, height_y + y, 0);
                block_count++;
                x += 1;
            }
            else if (t == '+') {
                GameObject obj = Instantiate(ironPrefab);
                obj.transform.position = new Vector3(x, height_y + y, 0);
                block_count++;
                x += 1;
            }
            else if (t == '\\')
            {
                y--;
                x = -(width_x - 1) / 2;

            }
            else if(t == ' ')
            {
                x += 1;
            }
        }
        //for (int i = 0; i < width_y; i++)
        //{
        //    for (int j = -(width_x - 1) / 2; j < (width_x + 1) / 2; j++)
        //    {
        //        GameObject obj = Instantiate(blockPrefab);
        //        obj.GetComponent<Renderer>().material.color = UnityEngine.Random.ColorHSV();
        //        obj.transform.position = new Vector3(j, height_y + i, 0);
        //        block_count += 1;
        //    }
        //}
    }

    private void SetIron()
    {
        for (int j = -(width_x - 1) / 2-1; j < (width_x + 1) / 2+1; j++)
        {
            GameObject obj = Instantiate(ironPrefab);
            obj.transform.position = new Vector3(j, height_y+width_y+1, 0);
        }
    }

    public void Random_Item(Vector3 pos)
    {
        if(UnityEngine.Random.Range(0, 5) == 0)
        {
            int rand = UnityEngine.Random.Range(0, ItemPrefabs.Length);
            GameObject obj = Instantiate(ItemPrefabs[rand]);
            obj.transform.position = pos;
        }
    }

    public int GetItemNum() { return ItemPrefabs.Length; }
}
