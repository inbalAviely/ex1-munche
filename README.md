# ex1-munche
We need to develop an algorithm that control elevators.
In off-line algorithm we get all the calls before the movements start.
the problem is to devide the calls between the elevators in the form that will lead to the minimum time pear call.
our research:
https://blog.birost.com/a?ID=00450-d7c47455-0bd9-42bd-bd9d-d790532c1010
https://en.wikipedia.org/wiki/Elevator_algorithm

off-line algorithm
we declare for each elevator an array that contain 
all the floor it needs to stop and when it needs to stop their.
we go over the calls and for each call we look where is the elevator
 in that moment and in what direction it goes.
 then we find thee closest elevator in rest and if all the elevator are not in rest
  we look for the elevator in the same direction of the call that have the least calls.
  if there is no elevator that answer this condition we add 5 seconds to the call and look again.
  after we find the elevator we add the call to array of the elevator.