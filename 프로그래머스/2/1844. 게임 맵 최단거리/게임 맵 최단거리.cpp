#include <vector>
#include <queue>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int rows = maps.size();
    int cols = maps[0].size();
    
    const vector<int> dx = {1,-1,0,0};
    const vector<int> dy = {0,0,1,-1};
    
    queue<vector<int>> q;
    q.push({0,0,1});
    maps[0][0] = 0;
    
    while (!q.empty()) {
        int x = q.front()[0];
        int y = q.front()[1];
        int count = q.front()[2];
        q.pop();
        
        for(int i = 0; i < 4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if (new_x >= 0 && new_x < rows && new_y >= 0 && new_y < cols) {
                if (new_x == rows-1 && new_y == cols-1) {
                    return count+1;
                }
                if (maps[new_x][new_y] == 1) {
                    q.push({new_x,new_y,count+1});
                    maps[new_x][new_y] = 0;
                }
            }
        }
    }
    return -1;
}