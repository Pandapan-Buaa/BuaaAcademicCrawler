import request from '@/utils/request'

export function getMultiIdScholars() {
  return request({
    url: '/mongo/getMultiIdScholars/',
    method: 'get'
  })
}
export function updateMultiIdScholarById(id, zhituId) {
  return request({
    url: '/mongo/updateMultiIdScholarById/',
    method: 'post',
    params: {
      id: id,
      zhituId: zhituId
    }
  })
}
