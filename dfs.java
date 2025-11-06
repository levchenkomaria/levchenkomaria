import java.util.*;

public class DFS {
    public static class DFSResult {
        public int[] timeIn;
        public int[] timeOut;
        
        public DFSResult(int[] timeIn, int[] timeOut) {
            this.timeIn = timeIn;
            this.timeOut = timeOut;
        }
    }
    
    public static DFSResult dfs(List<List<Integer>> graph, int startVertex) {
        int n = graph.size();
        boolean[] visited = new boolean[n];
        int[] timeIn = new int[n];
        int[] timeOut = new int[n];
        int[] timer = {0};
        
        dfsRecursive(graph, startVertex, visited, timeIn, timeOut, timer);
        
        return new DFSResult(timeIn, timeOut);
    }
    
    private static void dfsRecursive(List<List<Integer>> graph, int v, 
                                   boolean[] visited, int[] timeIn, 
                                   int[] timeOut, int[] timer) {
        visited[v] = true;
        timeIn[v] = timer[0];
        timer[0]++;
        
        for (int neighbor : graph.get(v)) {
            if (!visited[neighbor]) {
                dfsRecursive(graph, neighbor, visited, timeIn, timeOut, timer);
            }
        }
        
        timeOut[v] = timer[0];
        timer[0]++;
    }
}