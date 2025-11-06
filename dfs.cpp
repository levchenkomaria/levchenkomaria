#include <vector>
using namespace std;

pair<vector<int>, vector<int>> dfs(vector<vector<int>>& graph, int start_vertex) {
    int n = graph.size();
    vector<bool> visited(n, false);
    vector<int> time_in(n, 0);
    vector<int> time_out(n, 0);
    int timer = 0;
    
    function<void(int)> dfs_recursive = [&](int v) {
        visited[v] = true;
        time_in[v] = timer;
        timer++;
        
        for (int neighbor : graph[v]) {
            if (!visited[neighbor]) {
                dfs_recursive(neighbor);
            }
        }
        
        time_out[v] = timer;
        timer++;
    };
    
    dfs_recursive(start_vertex);
    return {time_in, time_out};
}
