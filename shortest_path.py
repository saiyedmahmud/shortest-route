
graph = {
  "Rabat": {"Sueca":1063,"Hamburg": 30 },
  "Sueca":{"Rudow":2656,"Rabat":1063 },
  "Rudow":{"Mosu":1352,"Sueca":2656},
  "Mosu":{"Le Plessis Trevise":1841,"Rudow":1352 },
  "Le Plessis Trevise":{"Kang Dong":61,"Mosu":1841 },
  "Kang Dong":{"Nezahualcóyot":1634,"Le Plessis Trevise":61},
  "Nezahualcóyot":{"Lindenwold":151,"Kang Dong":1634 },
  "Lindenwold":{"Queanbeyan":285,"Lindenwold":151 },
  "Queanbeyan":{"Saint Chamond":146 },
  "Saint Chamond":{"Cheektowaga":11,"Queanbeyan":146 },
  "Cheektowaga":{"Tirupati":380,"Saint Chamond":11},
  "Tirupati":{"Snezhinsk":2547,"Cheektowaga":380 },
  "Snezhinsk":{"Glazov":2524,"Tirupati":2547},
  "Glazov":{"Gaoyou":97,"Snezhinsk":2524},
  "Gaoyou":{"Nola":6999,"Glazov":97 },
  "Nola":{"Rutigliano":63,"Gaoyou":6999},
  "Rutigliano":{"Colombo":105,"Nola":63 },
  "Colombo":{"Meckenheim":244, "Rutigliano": 105},
  "Meckenheim":{"Hamburg":502,'Colombo': 244},
  "Hamburg":{"Meckenheim":502},

}


def route_distance(graph,start): 
    print("Source node is Rabat")
    end = input("Enter the Destination: ").capitalize() 
    shortest_distance = {} 
    track_predecessor = {} 
    unvisited = graph 
    infinity = float('inf')
    track_route = [] 





    for node in unvisited:
        shortest_distance[node] = infinity

    shortest_distance[start] = 0


    while unvisited:
        min_distance = None

        for node in unvisited:
            if min_distance is None:
                min_distance = node

            elif shortest_distance[node] < shortest_distance[min_distance]:
                min_distance = node



        path_options = graph[min_distance].items()




        for child_node, weight in path_options:

            if weight + shortest_distance[min_distance] < shortest_distance[child_node]:

                shortest_distance[child_node] = weight + shortest_distance[min_distance]

                track_predecessor[child_node] = min_distance


        unvisited.pop(min_distance)




    currentNode = end

    while currentNode != start:

        try:
            track_route.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    track_route.insert(0,start)


    if shortest_distance[end] != infinity:
      print(f'The Shortest route of {start} to {end} is:  ')
      print(track_route)
      print(f'And the distance is {str(shortest_distance[end])} km')
        

route_distance(graph,start='Rabat')