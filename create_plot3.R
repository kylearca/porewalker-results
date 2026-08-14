TAB <- read.table("chikv6khexamer-table-fm.txt", header=FALSE)
postscript("chikv6khexamer-Rplot3.eps", horizontal=FALSE, onefile=FALSE,
                  height=4, width=4, pointsize=10)
plot(TAB, type="l", col="blue", xlab="Pore axis (X-Coord)", ylab="Dia (Ang)", main="Pore diameter profile (3A)", lab=c(8, 10, 12))
dev.off()
q()
