# recompress gbx

small python util to recompress payloads of gbx files

saves about 10-20% by my testing.

will only work if there are no entries in the reference table of external nodes. (all items i've tested with are fine)

if developing: `python3 recompress.py`

Otherwise download the release and then follow:

## usage

via the release: run `.\path\to\recompress-gbx.exe MyCoolThing.Item.Gbx` for any .Gbx file.

The program should complain if it knows it will fail, but this is pretty rough so you know, it might think it makes something valid that isn't.

![image](https://user-images.githubusercontent.com/1046448/191520614-aca9a331-55cf-4954-90b5-a9d030446a15.png)

## benchmark

```
PS C:\Users\xertrov> cd .\Documents\Trackmania\
PS C:\Users\xertrov\Documents\Trackmania> cd .\recompress-demo\
PS C:\Users\xertrov\Documents\Trackmania\recompress-demo> $files = Get-ChildItem .\*.Gbx
PS C:\Users\xertrov\Documents\Trackmania\recompress-demo> foreach ($file in $files) {
>> ..\..\..\Downloads\recompress-gbx-v0.0.1\recompress-gbx.exe $file
>> }

# ---snip
# execution happens for 14 other items ...
# snip---

GBX-recompress 0.0.1.
Issues: https://github.com/XertroV/gbx-recompress/issues
Contact: @XertroV on Openplanet discord.

Writing recompressed file: wide finish ring_recompressed.Block.Gbx

# Recompressing:

Input: C:\Users\xertrov\Documents\Trackmania\recompress-demo\wide finish ring.Block.Gbx
Output: wide finish ring_recompressed.Block.Gbx (in the local directory)

## Recompression status:

- Original file:    1025 KB
- Recompressed:      829 KB

Done.

PS C:\Users\xertrov\Documents\Trackmania\recompress-demo> ls


    Directory: C:\Users\xertrov\Documents\Trackmania\recompress-demo


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        21/09/2022  11:37 PM        1623538 00-SausageDirt-DiagRightLoop11X.Block.Gbx
-a----        21/09/2022  11:39 PM        1382855 00-SausageDirt-DiagRightLoop11X_recompressed.Block.Gbx
-a----        21/09/2022  11:36 PM         689550 ArenaCPNFX2.Block.Gbx
-a----        21/09/2022  11:39 PM         567305 ArenaCPNFX2_recompressed.Block.Gbx
-a----        21/09/2022  11:36 PM         446655 C_RockArch.Item.Gbx
-a----        21/09/2022  11:39 PM         389881 C_RockArch_recompressed.Item.Gbx
-a----        21/09/2022  11:36 PM        1054199 dirtice12.Block.Gbx
-a----        21/09/2022  11:39 PM         849030 dirtice12_recompressed.Block.Gbx
-a----        21/09/2022  11:37 PM        1623063 dirtice86.Block.Gbx
-a----        21/09/2022  11:39 PM        1383019 dirtice86_recompressed.Block.Gbx
-a----        21/09/2022  11:36 PM        1697752 DirtTechBranchStraightX4Right.Block.Gbx
-a----        21/09/2022  11:39 PM        1345053 DirtTechBranchStraightX4Right_recompressed.Block.Gbx
-a----        21/09/2022  11:37 PM        1526908 DirtTechCheckpointSlopeDown.Block.Gbx
-a----        21/09/2022  11:39 PM        1337570 DirtTechCheckpointSlopeDown_recompressed.Block.Gbx
-a----        21/09/2022  11:36 PM        1820441 ice-3-way.Block.Gbx
-a----        21/09/2022  11:39 PM        1465370 ice-3-way_recompressed.Block.Gbx
-a----        21/09/2022  11:36 PM        1022646 Map In A Bottle.Item.Gbx
-a----        21/09/2022  11:39 PM         836218 Map In A Bottle_recompressed.Item.Gbx
-a----        21/09/2022  11:36 PM        1303782 OriginalStadiumStart.Block.Gbx
-a----        21/09/2022  11:39 PM        1077111 OriginalStadiumStart_recompressed.Block.Gbx
-a----        21/09/2022  11:36 PM        1751126 RoadTechDoubleMultilap.Block.Gbx
-a----        21/09/2022  11:39 PM        1432008 RoadTechDoubleMultilap_recompressed.Block.Gbx
-a----        21/09/2022  11:36 PM         724689 TallJapaneseMaple.Item.gbx
-a----        21/09/2022  11:39 PM         660886 TallJapaneseMaple_recompressed.Item.gbx
-a----        21/09/2022  11:36 PM        1081653 tinyfin.Item.Gbx
-a----        21/09/2022  11:39 PM         865307 tinyfin_recompressed.Item.Gbx
-a----        21/09/2022  11:36 PM        1025544 wide finish ring.Block.Gbx
-a----        21/09/2022  11:39 PM         829832 wide finish ring_recompressed.Block.Gbx
```
