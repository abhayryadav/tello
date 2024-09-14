# from djitellopy import tello
# from time import sleep
#
# mytello = tello.Tello()
# mytello.connect()
# i=5;
# while(i):
#     print(mytello.get_battery())
#     i -=1
# mytello.takeoff()
# mytello.send_rc_control(0,1,0,0)
# sleep(1)
# mytello.send_rc_control(0,-1,0,0)
# mytello.send_rc_control(0,0,0,0)
# mytello.land()
#
#



#
# from djitellopy import tello
# from time import sleep
# import cv2
#
# mytello = tello.Tello()
# mytello.connect()
#
# print("Battery level:", mytello.get_battery())
# mytello.streamon()
#
#
# framer = mytello.get_frame_read()
# if framer.cap.isOpened():
#     print("Stream is open")
# else:
#     print("Stream is not open")
#
# try:
#     while True:
#         img = framer.frame
#         if img is None:
#             print("Failed to retrieve frame")
#             break
#         cv2.imshow("image", img)
#         cv2.waitKey(1)
# finally:
#     cv2.destroyAllWindows()
#     mytello.streamoff()
#     mytello.end()



# errorss
# from djitellopy import Tello
# import cv2
#
# my_drone = Tello()
# my_drone.connect()
# print(my_drone.get_battery())
# my_drone.streamon()
# while True:
#     # Read a frame from the video stream
#     img = my_drone.get_frame_read().frame
#     img = cv2.resize(img, (360, 240))
#     # Display the frame
#     cv2.imshow("Image", img)
#     # Check for key press to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()
# my_drone.streamoff()
# my_drone.land()







# #tello

# # empty frames
# from djitellopy import Tello
# import cv2
# import time
# import collections

# # Initialize the Tello drone
# tello = Tello()
# tello.connect()

# # Start the video stream
# tello.streamon()

# # Initialize a buffer to store the frames
# frame_buffer = collections.deque(maxlen=10)  # Adjust buffer size as needed

# try:
#     while True:
#         try:
#             # Retrieve the latest frame from the drone's camera
#             frame = tello.get_frame_read().frame
#             frame_buffer.append(frame)

#             # Get the most recent frame from the buffer
#             img = frame_buffer[-1]

#             # Display the frame in a window
#             cv2.imshow('Tello Video Stream', img)

#             # Exit if the 'q' key is pressed
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         except Exception as e:
#             print(f"Error retrieving frame: {e}")
#             time.sleep(1)
#             continue

# except KeyboardInterrupt:
#     print("Interrupted by user, stopping...")

# finally:
#     # Release resources
#     tello.streamoff()
#     cv2.destroyAllWindows()
#     tello.end()
#     print("Stream ended.")






