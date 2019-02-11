#include<bits/stdc++.h>

using namespace std;

inline int read()
{
    char ch=getchar();
    int f=1,x=0;
    while (ch<'0' || ch>'9')
    {
        if (ch=='-') f=-1;
        ch=getchar();
    }
    while (ch>='0' && ch<='9')
    {
        x=x*10+ch-'0';
        ch=getchar();
    }
    return f*x;
}

struct MAP{
    int s[10][10];
} stat;
int n,m,a,b,c,cur[10][3]; //0->x;1->y;2->left/right
bool can=0;
bool mark[10][10];

inline void drop()
{
    for (int i=1;i<=5;i++)
    {
        for (int j=1;j<=7;j++)
        {
            if (!mark[i][j]) continue;
            mark[i][j]=0;
            stat.s[i][j]=0;
        }
        for (int j=1;j<=7;j++)
        {
            if (stat.s[i][j]) continue; //找到空格删除
            int cnt=0;
            for (int k=j+1;k<=7;k++)
            {
                if (!stat.s[i][k]) continue;
                stat.s[i][j+cnt]=stat.s[i][k];
                cnt++;
                stat.s[i][k]=0;
                break;
            }
        }
    }
}

inline void mv(int x,int y,int s) //保证没有越界
{
    swap(stat.s[x][y],stat.s[x+s][y]);
    drop();
}

inline bool check()
{
    for (int i=1;i<=5;i++)
        if (stat.s[i][1])
            return 0;
    return 1;
}

bool dfs_update(int x,int y,int fx,int fy,int step) //标记所有可以消除的
{
    bool can;
    if (step>=3) can=1;
    else can=0;
    if (stat.s[x+fx][y+fy]==stat.s[x][y]) can=can || dfs_update(x+fx,y+fy,fx,fy,step+1);
    if (can) mark[x][y]=1;
    return can;
}

inline bool update() //消去所有可以消的方块
{
    for (int i=1;i<=5;i++)
    {
        for (int j=1;j<=7;j++)
        {
            if (!stat.s[i][j]) continue;
            dfs_update(i,j,0,1,1); //纵向上
            dfs_update(i,j,0,-1,1); //纵向下
            dfs_update(i,j,1,0,1); //横向右
            dfs_update(i,j,-1,0,1); //横向左
        }
    } //mark checked
    int marked=0;
    for (int i=1;i<=5;i++)
        for (int j=1;j<=7;j++)
            marked+=mark[i][j];
    drop();
    return marked;
}

void dfs(int step)
{
    if (can) return;
    if (check()) //已经全部消除完，校验每列第一个即可
    {
        can=1;
        for (int i=1;i<step;i++) printf("%d %d %d\n",cur[i][0]-1,cur[i][1]-1,cur[i][2]);
        return;
    }
    if (step==n+1) return;
    MAP now;
    for (int i=1;i<=5;i++)
        for (int j=1;j<=7;j++)
            now.s[i][j]=stat.s[i][j]; //备份
    for (int i=1;i<=5;i++)
    {
        for (int j=1;j<=7;j++)
        {
            if (!now.s[i][j]) continue;
            if (i==5) //只可能往左移
            {
                if (now.s[i-1][j]) continue;
                mv(i,j,-1);
                cur[step][0]=i; cur[step][1]=j; cur[step][2]=-1;
                while (update());
                dfs(step+1);
                for (int i=1;i<=5;i++)
                    for (int j=1;j<=7;j++)
                        stat.s[i][j]=now.s[i][j];
                continue;
            }

            // 右移
            if (stat.s[i][j]!=stat.s[i+1][j])
            {
                mv(i,j,1);
                cur[step][0]=i; cur[step][1]=j; cur[step][2]=1;
                while (update());
                dfs(step+1);
                for (int i=1;i<=5;i++)
                    for (int j=1;j<=7;j++)
                        stat.s[i][j]=now.s[i][j];
            }
            
            if (i>=2 && !now.s[i-1][j]) //左边为空往左移
            {
                mv(i,j,-1);
                cur[step][0]=i; cur[step][1]=j; cur[step][2]=-1;
                while (update());
                dfs(step+1);
                for (int i=1;i<=5;i++)
                    for (int j=1;j<=7;j++)
                        stat.s[i][j]=now.s[i][j];
            }
        }
    }
}

int main()
{
    n=read();
    for (int i=1;i<=5;i++)
    {
        int m=0;
        a=read();
        while (a) 
        {
            stat.s[i][++m]=a;
            a=read();
        }
    } //read checked
    dfs(1);
    if (!can) printf("-1");
    return 0;
}