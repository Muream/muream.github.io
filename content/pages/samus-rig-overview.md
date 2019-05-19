---
Title: Samus Rig Overview
typora-root-url: ../
---

## Body rig

This is still very WIP. Most of the logic is there bit it's lacking a few controls for the armor bits and I have barely worked on the skinning. :)

### Spine

The spine is fairly simple. Just an FK chain with a reverse pelvis control.  
You can individually scale each control of the spine to get some squash and stretch.

<video autoplay loop muted controls playsinline width="100%" height="auto" src="/images/samus-rig-overview/spine.webm"></video>

Notes: 

- The scale doesn't work when scaling all the controls at the same time for some reason so you need to scale them one at a time.
- The top of the chest armor scales way too  much, I'll need to fix that.

### Limbs

All the limbs (arms and legs) have the same overall setup most of their settings are located on the settings controls.

![Settings Controls](/images/samus-rig-overview/settings-controls.png)

- They have an FK and IK mode that you can switch between. Very straight forward so no gifs for this one. 

- In IK mode, you can decide whether you want to have  the limb stretching to reach the IK control or not.
  This slider is located on the IK control and goes from 0 to 1.  
  0 means no stretch and 1 means full stretch. The value is at 0.15 by default which seems to provide a nice behavior and seriously limits IK Popping. 
  If you want another default value for this, just ask!
  
  <video autoplay loop muted controls playsinline width="100%" height="auto" src="/images/samus-rig-overview/stretch-ik.webm"></video>
  
- The secondary controls (hidden by default) allow you bend the limb and move the knee/elbow pretty much how you want.
  This is setup in a way that you can basically consider the secondary controls as handles on a Bezier curve.
  
  <video autoplay loop muted controls playsinline width="100%" height="auto" src="/images/samus-rig-overview/secondary-controls.webm"></video>
  
  
  Keep in mind that this behavior is layered on top of the IK or FK behavior.

#### A few arm specific settings

- They are in FK mode by default
- When In FK you can toggle the "Inherit Rotation" so that the arms follow or not the rotation of the body.
  
  <video autoplay loop muted controls playsinline width="100%" height="auto" src="/images/samus-rig-overview/arms-inherit-rotation.webm"></video>

#### A few leg specific settings

- They are in IK mode by default

- When in IK mode, you have a few settings on the IK control:

  - Foot Roll: A positive value will make the foot roll forward while a negative will make the foot roll on the heel.
  - Bend Angle: Angle at which the Forward foot roll starts rotating on the tip of the foot. (The higher, the later the tip will rotate)
  - Bank: Rolls the foot from side to side. A negative value will roll towards the interior and a positive value will roll towards the exterior.

<video autoplay loop muted controls playsinline width="100%" height="auto" src="/images/samus-rig-overview/foot-roll.webm"></video>



## Face Rig

The face rig is still very limited and what's implemented is very straight forward so there's not much to say right now.

### A few notes:

Due to [a crash](https://developer.blender.org/T64512) with bones custom shapes in recent builds of blender, I had to remove them as well as remove the fact that they were attached on the face.
These features will come back once The crash is fixed.

I had to disable the jaw control as there was some double transformations when moving the body. This will be re-enabled as soon as I find a fix.