double findMedianSortedArrays(int* a, int nums1Size, int* b, int nums2Size) {
    int size_a = nums1Size;
    int size_b = nums2Size;
    int size = size_a+size_b;
    int c[size];
    for (int i = 0; i < size_a; i++){
        c[i] = a[i];
    }
    int x = 0;
    for (int i = size_a; i < size; i++){
        c[i] = b[x];
        x++;
    }

    int i,j,temp;
	for(i=0;i<size-1;i++)
	{
		for(j=0;j<size-1-i;j++)
		{
			if(c[j]>c[j+1])
			{
				temp=c[j];
				c[j]=c[j+1];
				c[j+1]=temp;
			}
		}
	}
	for(j=0;j<size;j++)
		{printf("%d",c[j]);}
	printf("\n%d",size);
		
	if((size%2)!=0){
        double y = c[(size/2)];
	    return y;
	}
	else{
	    double s,t,y;
	    s=c[(size/2)];
	    t=c[(size/2)-1];
	    y = (s+t)/2;
	    return y;
	}
}