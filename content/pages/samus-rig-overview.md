---
Title: Samus Rig Overview
typora-root-url: ../
---

## Body rig

This is still very WIP. Most of the logic is there bit it's lacking a few controls for the armor bits and the I have barely worked on the skinning. :)

### Spine

The spine is fairly simple. Just an FK chain with a reverse pelvis control.
You can individually scale each control of the spine to get some squash and stretch.

You can individually scale each control of the spine to get some squash and stretch.

![Spine](/images/samus-rig-overview/spine.gif)

Notes: 

- The scale doesn't work when scaling all the controls at the same time for some reason so you need to scale them one at a time
- The top of the chest armor scales way too  much, I'll need to fix that

### Limbs

All the limbs (arms and legs) have the same overall setup most of their settings are located on the settings controls.

![Settings Controls](/images/samus-rig-overview/settings-controls.png)

- They have an FK and IK mode that you can switch between. Very straight forward so no gifs for this one. There's an IK/FK switch on the

- In IK, you can decide whether you want to have  the limb stretching to reach the IK control or not.
  This slider is located on the IK control and goes from 0 to 1. 0 means no stretch and 1 means full stretch. The value is at 0.15 by default which seems to provide a nice behavior and seriously limits IK Popping. 
  If you want another default value for this, just ask!
  ![Settings Controls](/images/samus-rig-overview/stretch-ik.gif)
  
- The secondary controls (hidden by default) allow you bend the limb and move the knee/elbow pretty much how you want.
  This is setup in a way that you can basically consider the secondary controls as handles on a Bezier curve.
  
  ![Settings Controls](/images/samus-rig-overview/secondary-controls.gif)
  Keep in mind that this behavior is layered on top of the IK or FK behavior.

#### A few arm specific settings

- They are In FK by default
- When In FK you can toggle the "Inherit Rotation" so that the arms follow or not the rotation of the body.